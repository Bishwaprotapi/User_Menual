### Page: Adjustment

![Adjustment: Screen](screenshots/transaction/adjustment.png)

**Page purpose:** This page provides navigation for various adjustment types within the Transaction module.

**Route:** `/transaction/adjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Adjustment", "task": "Navigate to adjustment sub-menus", "action": "view", "roles": [], "route": "/transaction/adjustment", "screenshots": ["screenshots/transaction/adjustment.png"], "keywords": ["adjustment", "debit note", "credit note", "VDS adjustment", "other adjustment"], "task_order": 1} -->
#### Task: Navigate to adjustment sub-menus

**Purpose:** Access specific adjustment modules like Debit Note, Credit Note, VDS, or Other Adjustment.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in

**Steps:**
1. Click on TRANSACTION in the side menu
2. Click on Adjustment to expand the list
3. Select the desired adjustment sub-menu

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The application redirects to the selected adjustment page.

**Warnings:**
* No specific warning was identified

**Search keywords:** adjustment, debit note, credit note, VDS adjustment, other adjustment

### Page: Credit Note Adjustment

![Credit Note Adjustment: Screen](screenshots/transaction/credit_note_adjustment.png)

![Credit Note Adjustment: Show](screenshots/transaction/credit_note_adjustment_show.png)

**Page purpose:** Allows users to search and view credit note adjustments.

**Route:** `/transaction/adjustment/creditNoteAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Credit Note Adjustment", "task": "Filter and view credit note adjustments", "action": "view", "roles": [], "route": "/transaction/adjustment/creditNoteAdjustment", "screenshots": ["screenshots/transaction/credit_note_adjustment.png", "screenshots/transaction/credit_note_adjustment_show.png"], "keywords": ["credit note", "search", "filter", "view"], "task_order": 1} -->
#### Task: Filter and view credit note adjustments

**Purpose:** To locate and review specific credit note adjustments by date range and branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Transaction/Adjustment

**Steps:**
1. Navigate to Credit Note Adjustment
2. Select a branch from the dropdown
3. Enter the 'From Date' and 'To Date'
4. Click 'View'

**Fields and controls:**
* **Branch:** The business unit for the adjustment.
* **Enter From Date:** Start date for the search range.
* **Enter To Date:** End date for the search range.
* **Code Invoice Search:** Search for a specific invoice code.

**Expected result:** A table of credit note adjustments matching the search criteria appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, search, filter, view

### Page: Debit Note Adjustment

![Debit Note Adjustment: Screen](screenshots/transaction/debit_note_adjustment.png)

![Debit Note Adjustment: Show](screenshots/transaction/debit_note_adjustment_show.png)

**Page purpose:** Management page for viewing and creating debit note adjustments.

**Route:** `/transaction/adjustment/debitNoteAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Debit Note Adjustment", "task": "Search debit note adjustments", "action": "search", "roles": [], "route": "/transaction/adjustment/debitNoteAdjustment", "screenshots": ["screenshots/transaction/debit_note_adjustment.png", "screenshots/transaction/debit_note_adjustment_show.png"], "keywords": ["debit note", "search", "list"], "task_order": 1} -->
#### Task: Search debit note adjustments

**Purpose:** To find existing debit note records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Transaction/Adjustment

**Steps:**
1. Select the branch from the dropdown
2. Set the date range
3. Optionally enter a Debit Note Code in the search field
4. Click 'View'

**Fields and controls:**
* **Select Branch:** Select the relevant branch.
* **Debit Note Code Search:** Search by specific debit note code.

**Expected result:** Matching records populate the result table.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, search, list

### Page: Other Adjustment

![Other Adjustment: Screen](screenshots/transaction/other_adjustment.png)

**Page purpose:** Displays miscellaneous VAT/Tax adjustments.

**Route:** `/transaction/adjustment/otherAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Other Adjustment", "task": "View other adjustments", "action": "view", "roles": [], "route": "/transaction/adjustment/otherAdjustment", "screenshots": ["screenshots/transaction/other_adjustment.png"], "keywords": ["other adjustment", "miscellaneous", "tax records"], "task_order": 1} -->
#### Task: View other adjustments

**Purpose:** Monitor and review various tax adjustment records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Transaction/Adjustment

**Steps:**
1. Navigate to Other Adjustment
2. Review the generated list
3. Use pagination controls to browse records

**Fields and controls:**
* **Adjustment Code Search:** Field to filter by adjustment code.
* **rows per page:** Set the number of records displayed.

**Expected result:** A comprehensive list of adjustments is displayed with details like purpose, type, and amount.

**Warnings:**
* No specific warning was identified

**Search keywords:** other adjustment, miscellaneous, tax records

### Page: User Profile

![Transaction: Screen](screenshots/transaction/transaction.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/transaction`

<!-- manual-meta: {"module": "Transaction", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/transaction", "screenshots": ["screenshots/transaction/transaction.png"], "keywords": ["User Profile", "transaction"], "task_order": 1} -->
#### Task: Use User Profile

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the User Profile page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** User Profile, transaction

### Page: VDS Adjustment

![Treasury And Others: Screen](screenshots/transaction/treasury_and_others.png)

![Treasury And Others: Show](screenshots/transaction/treasury_and_others_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/transaction/treasuryAndOthers`

<!-- manual-meta: {"module": "Transaction", "page": "VDS Adjustment", "task": "Use VDS Adjustment", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/transaction/treasuryAndOthers", "screenshots": ["screenshots/transaction/treasury_and_others.png", "screenshots/transaction/treasury_and_others_show.png"], "keywords": ["VDS Adjustment", "treasury and others"], "task_order": 1} -->
#### Task: Use VDS Adjustment

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the VDS Adjustment page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.
* **Pending:** Visible radio control.
* **Complete:** Visible radio control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** VDS Adjustment, treasury and others

### Page: Treasury Deposit

![Treasury Deposit: Screen](screenshots/transaction/treasury_deposit.png)

**Page purpose:** Manages records of treasury deposits and challan details.

**Route:** `/transaction/treasuryAndOthers/treasuryDeposit`

<!-- manual-meta: {"module": "Transaction", "page": "Treasury Deposit", "task": "Search treasury deposits", "action": "search", "roles": [], "route": "/transaction/treasuryAndOthers/treasuryDeposit", "screenshots": ["screenshots/transaction/treasury_deposit.png"], "keywords": ["treasury deposit", "challan", "search"], "task_order": 1} -->
#### Task: Search treasury deposits

**Purpose:** Locate specific treasury deposit records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Treasury and Others

**Steps:**
1. Enter the Treasury Code or Challan No in the search field
2. Review the table results

**Fields and controls:**
* **Tresuary Code and Challan No Search:** Input for searching specific deposit codes or challans.

**Expected result:** Filtered table results displayed based on the search query.

**Warnings:**
* No specific warning was identified

**Search keywords:** treasury deposit, challan, search

### Page: Turnover Tax

![Turnover Tax: Screen](screenshots/transaction/turnover_tax.png)

![Turnover Tax: Show](screenshots/transaction/turnover_tax_show.png)

**Page purpose:** Tool for viewing turnover tax-related transactions.

**Route:** `/transaction/treasuryAndOthers/turnoverTax`

<!-- manual-meta: {"module": "Transaction", "page": "Turnover Tax", "task": "Filter turnover tax transactions", "action": "filter", "roles": [], "route": "/transaction/treasuryAndOthers/turnoverTax", "screenshots": ["screenshots/transaction/turnover_tax.png", "screenshots/transaction/turnover_tax_show.png"], "keywords": ["turnover tax", "filter"], "task_order": 1} -->
#### Task: Filter turnover tax transactions

**Purpose:** Review turnover tax entries for a specific branch and time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Treasury and Others

**Steps:**
1. Select the branch
2. Set the date range
3. Click 'View'

**Fields and controls:**
* **Select Branch:** Filter by business branch.
* **Enter From Date:** Start of search period.
* **Enter To Date:** End of search period.

**Expected result:** Table displays relevant turnover tax data.

**Warnings:**
* No specific warning was identified

**Search keywords:** turnover tax, filter

### Page: VDS Adjustment

![Vds Adjustment: Screen](screenshots/transaction/vds_adjustment.png)

![Vds Adjustment: Show](screenshots/transaction/vds_adjustment_show.png)

**Page purpose:** This page allows users to view and manage adjustments related to VAT Deducted at Source (VDS).

**Route:** `/transaction/adjustment/vdsAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "VDS Adjustment", "task": "Filter VDS adjustments", "action": "filter", "roles": [], "route": "/transaction/adjustment/vdsAdjustment", "screenshots": ["screenshots/transaction/vds_adjustment.png", "screenshots/transaction/vds_adjustment_show.png"], "keywords": ["VDS", "Adjustment", "Filter", "Search", "VAT"], "task_order": 1} -->
#### Task: Filter VDS adjustments

**Purpose:** To find specific VDS adjustment records based on branch, date range, and status.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Transaction module.

**Steps:**
1. Navigate to Transaction > Adjustment > VDS Adjustment.
2. Select the 'Select Branch' from the dropdown menu.
3. Enter the date range using 'Enter From Date' and 'Enter To Date'.
4. Select a status: 'Pending' or 'Complete'.
5. Click the 'View' button to display the filtered records.

**Fields and controls:**
* **Select Branch:** Dropdown to select the company branch.
* **Enter From Date:** Start date for the filter.
* **Enter To Date:** End date for the filter.
* **Pending:** Radio button to filter records with pending status.
* **Complete:** Radio button to filter records with completed status.

**Expected result:** A list of VDS adjustment records matching the specified criteria will appear in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, Adjustment, Filter, Search, VAT

### Page: VDS Certificate (Issue)

![Vds Certificate Issue: Screen](screenshots/transaction/vds_certificate_issue.png)

![Vds Certificate Issue: Show](screenshots/transaction/vds_certificate_issue_show.png)

**Page purpose:** This page is used to view issued VAT Deduct at Source (VDS) certificates.

**Route:** `/transaction/treasuryAndOthers/varDeductatSource`

<!-- manual-meta: {"module": "Transaction", "page": "VDS Certificate (Issue)", "task": "View VDS certificates", "action": "view", "roles": [], "route": "/transaction/treasuryAndOthers/varDeductatSource", "screenshots": ["screenshots/transaction/vds_certificate_issue.png", "screenshots/transaction/vds_certificate_issue_show.png"], "keywords": ["VDS", "Certificate", "Issue", "Deduct", "VAT"], "task_order": 1} -->
#### Task: View VDS certificates

**Purpose:** To view and track issued VDS certificates for a specific period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Transaction module.

**Steps:**
1. Navigate to Transaction > Treasury And Others > VDS Certificate (Issue).
2. Select the branch from 'Select Branch'.
3. Specify the date range using 'Enter From Date' and 'Enter To Date'.
4. Choose a status: 'All', 'Pending', or 'Complete'.
5. Click the 'View' button.

**Fields and controls:**
* **Select Branch:** Dropdown for branch selection.
* **Enter From Date:** Start date for the period.
* **Enter To Date:** End date for the period.
* **All:** Filter by all certificate statuses.
* **Pending:** Filter by pending certificate status.
* **Complete:** Filter by completed certificate status.

**Expected result:** A table showing details like Purchase Date, Supplier Name, Certificate No, Chalan No, and Deducted Amount will be generated.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, Certificate, Issue, Deduct, VAT