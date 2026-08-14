#!/usr/bin/env python3

"""
Automated ligand library preparation for G-quadruplex molecular docking.

Workflow:
    SDF input
        ↓
    3D structure generation
        ↓
    Geometry optimization
        ↓
    Protonation/hydrogen handling at specified pH
        ↓
    Gasteiger partial charge assignment
        ↓
    PDBQT output

Designed for execution in WSL2 Ubuntu using Open Babel.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_INPUT = "raw_compounds"
DEFAULT_OUTPUT = "prepared_ligands_pdbqt"
DEFAULT_PH = 7.0


def check_openbabel():
    """Verify that the Open Babel executable is available."""

    if shutil.which("obabel") is None:
        print("ERROR: Open Babel ('obabel') was not found in PATH.")
        print("Please install Open Babel and verify it with:")
        print("    obabel -V")
        sys.exit(1)

    try:
        result = subprocess.run(
            ["obabel", "-V"],
            capture_output=True,
            text=True,
            check=True
        )

        version = result.stdout.strip() or result.stderr.strip()
        print(f"Open Babel detected: {version}")

    except subprocess.CalledProcessError as error:
        print(f"ERROR: Unable to execute Open Babel: {error}")
        sys.exit(1)


def prepare_ligand(input_path, output_path, ph):
    """
    Prepare a single ligand using Open Babel.

    Steps:
        1. Generate a 3D structure.
        2. Optimize the generated geometry.
        3. Adjust protonation/hydrogen handling at the specified pH.
        4. Assign Gasteiger partial charges.
        5. Write the prepared ligand as PDBQT.
    """

    command = [
        "obabel",
        str(input_path),
        "-O",
        str(output_path),
        "--gen3d",
        "-p",
        str(ph),
        "--partialcharge",
        "gasteiger"
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return True, result.stdout, result.stderr

    except subprocess.CalledProcessError as error:
        return False, error.stdout, error.stderr


def prepare_g4_stabilizer_library(
    input_folder=DEFAULT_INPUT,
    output_folder=DEFAULT_OUTPUT,
    ph=DEFAULT_PH
):
    """
    Automatically prepare all SDF ligands in the input directory.

    Parameters
    ----------
    input_folder : str
        Directory containing raw SDF ligand structures.

    output_folder : str
        Directory where prepared PDBQT files will be written.

    ph : float
        Target pH used for Open Babel protonation/hydrogen handling.
    """

    input_path = Path(input_folder)
    output_path = Path(output_folder)

    print("=" * 75)
    print("G4 / R-LOOP LIGAND LIBRARY PREPARATION")
    print("=" * 75)

    print("\n[1] Checking computational environment...")
    check_openbabel()

    # ------------------------------------------------------------------
    # Directory preparation
    # ------------------------------------------------------------------

    if not input_path.exists():
        input_path.mkdir(parents=True, exist_ok=True)

        print(f"\nInput directory did not exist.")
        print(f"Created: {input_path}")
        print("Add .sdf ligand structures to this directory and rerun.")

        return

    output_path.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Discover ligand library
    # ------------------------------------------------------------------

    sdf_files = sorted(input_path.glob("*.sdf"))

    print(f"\n[2] Ligand library discovery")
    print("-" * 75)

    if not sdf_files:
        print(f"No .sdf files were found in:")
        print(f"    {input_path}")

        print("\nPipeline stopped: no ligand structures available.")
        return

    print(f"Input directory : {input_path}")
    print(f"Output directory: {output_path}")
    print(f"Target pH       : {ph}")
    print(f"Ligands detected: {len(sdf_files)}")

    for ligand in sdf_files:
        print(f"  - {ligand.name}")

    # ------------------------------------------------------------------
    # Ligand preparation
    # ------------------------------------------------------------------

    print("\n[3] Ligand preparation")
    print("-" * 75)

    successful = []
    failed = []

    for index, ligand in enumerate(sdf_files, start=1):

        output_file = output_path / f"{ligand.stem}.pdbqt"

        print(
            f"\n[{index}/{len(sdf_files)}] "
            f"Preparing: {ligand.name}"
        )

        success, stdout, stderr = prepare_ligand(
            ligand,
            output_file,
            ph
        )

        if success and output_file.exists():

            successful.append(ligand.name)

            print("  Status : SUCCESS")
            print(f"  Output : {output_file}")

        else:

            failed.append(ligand.name)

            print("  Status : FAILED")

            if stderr.strip():
                print("  Open Babel error:")
                print(f"    {stderr.strip()}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    print("\n" + "=" * 75)
    print("LIGAND PREPARATION SUMMARY")
    print("=" * 75)

    print(f"Total ligands detected : {len(sdf_files)}")
    print(f"Successfully prepared  : {len(successful)}")
    print(f"Failed                 : {len(failed)}")

    if successful:
        print("\nSuccessful preparations:")

        for ligand in successful:
            print(f"  ✓ {ligand}")

    if failed:
        print("\nFailed preparations:")

        for ligand in failed:
            print(f"  ✗ {ligand}")

    # ------------------------------------------------------------------
    # Docking configuration summary
    # ------------------------------------------------------------------

    print("\n" + "=" * 75)
    print("AUTODOCK VINA CONFIGURATION")
    print("=" * 75)

    print("Target structure       : c-MYC G-quadruplex")
    print("Receptor               : 1XAV")
    print("Center X               : 14.85 Å")
    print("Center Y               : 2.30 Å")
    print("Center Z               : -11.40 Å")
    print("Search box             : 22 × 22 × 22 Å")
    print("Exhaustiveness         : 32")

    print("\nNote:")
    print(
        "The docking parameters above are reported for the subsequent "
        "AutoDock Vina stage. This script does not perform docking."
    )

    # ------------------------------------------------------------------
    # Final status
    # ------------------------------------------------------------------

    if failed:
        print("\nPipeline status: COMPLETED WITH ERRORS")
        print(
            "Review failed ligand preparations before proceeding "
            "to molecular docking."
        )
    else:
        print("\nPipeline status: LIGAND PREPARATION COMPLETED")
        print(
            "All detected SDF structures were successfully converted "
            "to docking-ready PDBQT files."
        )

    print("=" * 75)


def parse_arguments():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Prepare an SDF ligand library for AutoDock Vina "
            "using Open Babel."
        )
    )

    parser.add_argument(
        "--input",
        default=DEFAULT_INPUT,
        help=(
            "Directory containing raw SDF ligand structures "
            f"(default: {DEFAULT_INPUT})"
        )
    )

    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=(
            "Directory for prepared PDBQT structures "
            f"(default: {DEFAULT_OUTPUT})"
        )
    )

    parser.add_argument(
        "--ph",
        type=float,
        default=DEFAULT_PH,
        help=(
            "Target pH used for protonation/hydrogen handling "
            f"(default: {DEFAULT_PH})"
        )
    )

    return parser.parse_args()


def main():
    """Main program entry point."""

    args = parse_arguments()

    prepare_g4_stabilizer_library(
        input_folder=args.input,
        output_folder=args.output,
        ph=args.ph
    )


if __name__ == "__main__":
    main()
