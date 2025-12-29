# Implementation Plan: Card Face Organization

This document outlines the step-by-step plan to download and organize the card face images as requested.

## 1. Parse `card_face.md`

- Read the `card_face.md` file line by line.
- Determine the hierarchical structure (Issuer, Card Type, etc.) by analyzing the indentation of each line.
- Extract the following information for each card entry:
    - Card Name (e.g., "Amazon Business Prime")
    - Image URL (if present)
    - Any notes on the same line (e.g., "low res", "jpeg")
- Maintain the context of the current Issuer and categories while parsing.

## 2. Structure and Categorize Card Data

- For each extracted card, create a structured data object.
- Apply the specified logic to determine the final folder structure for each card:
    - **Issuer Folder**: This is the top-level folder (e.g., `American Express`, `Bank of America`). Per your instruction, `Others` will be treated as a single issuer.
    - **Card Type Sub-folder**:
        - Default to `Credit Card` if not explicitly `Debit Card`.
        - The `Business` and `Personal` categories imply `Credit Card`.
    - **Personal/Business Sub-folder**:
        - Default to `Personal` if not explicitly `Business`.
    - **Special Categories**:
        - **Others**: Cards under the `Others` issuer will be placed in `Others/[Debit|Credit]/[CardName]`, skipping the "Personal/Business" level.
        - **Virtual ID**: All cards from this section will be placed directly into a single top-level folder named `Virtual ID`.

## 3. File and Directory Operations

- For each card, perform the following:
    - **Create Directories**: Recursively create the full directory path determined in the previous step (e.g., `American Express/Credit Card/Business/`).
    - **Download Image or Create Dummy File**:
        - **If an image URL exists**:
            - Determine the correct file extension from the URL path or the associated notes ("jpeg" -> `.jpeg`).
            - Download the image from the URL and save it with the card's name (e.g., `Amazon Business Prime.png`).
        - **If no image URL exists**:
            - Create a small, blank placeholder image file (e.g., a 1x1 pixel bitmap) with the card's name (e.g., `Blue Business Cash.bmp`).
    - **Track Cards for README**: Keep a running list of all card names associated with each issuer.

## 4. Generate README.md Files

- After all file operations are complete, iterate through the list of issuers.
- For each issuer (excluding "Virtual ID"), create a `README.md` file in their root folder (e.g., `American Express/README.md`).
- Populate the `README.md` file with a markdown-formatted list of all the card names that belong to that issuer.
