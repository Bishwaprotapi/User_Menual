### Page: Audit Report

![Audit Report: Screen](screenshots/reports/audit_report.png)

**Page purpose:** This page provides an interface to access and manage audit-related data reports, including import, local purchase, local sales, and export activities.

**Route:** `/reports/otherReports/auditReport`

<!-- manual-meta: {"module": "Reports", "page": "Audit Report", "task": "View Audit Report Options", "action": "view", "roles": [], "route": "/reports/otherReports/auditReport", "screenshots": ["screenshots/reports/audit_report.png"], "keywords": ["audit", "report", "import", "sales", "purchase"], "task_order": 1} -->
#### Task: View Audit Report Options

**Purpose:** To see available categories of audit reports.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in

**Steps:**
1. Navigate to the Reports menu.
2. Click on 'Audit Report'.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The screen displays buttons for 'Import', 'Local Purchase', 'Local Sales', and 'Export'.

**Warnings:**
* No specific warning was identified

**Search keywords:** audit, report, import, sales, purchase

### Page: Chok Ka/Kha Report

![Chok Ka Kha: Screen](screenshots/reports/chok_ka_kha.png)

![Chok Ka Kha: Show](screenshots/reports/chok_ka_kha_show.png)

**Page purpose:** This page allows users to filter and view 'Chok Ka' and 'Chok Kha' report data by branch and date range.

**Route:** `/reports/otherReports/chok-ka/kha`

<!-- manual-meta: {"module": "Reports", "page": "Chok Ka/Kha Report", "task": "Filter Chok Ka/Kha Report", "action": "filter", "roles": [], "route": "/reports/otherReports/chok-ka/kha", "screenshots": ["screenshots/reports/chok_ka_kha.png", "screenshots/reports/chok_ka_kha_show.png"], "keywords": ["chok ka", "chok kha", "report", "filter"], "task_order": 1} -->
#### Task: Filter Chok Ka/Kha Report

**Purpose:** To retrieve report data for a specific branch and period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data exists for the selected criteria

**Steps:**
1. Select the 'Branch'.
2. Select the 'From Date'.
3. Select the 'To Date'.
4. Click 'View'.

**Fields and controls:**
* **Branch:** The specific branch to filter data by.
* **From Date:** Start date for the report range.
* **To Date:** End date for the report range.

**Expected result:** The report data will be displayed or a 'No Data Found' message will appear if no records match the criteria.

**Warnings:**
* If no records match, the interface will display 'No Data Found' for the report types.

**Search keywords:** chok ka, chok kha, report, filter

### Page: Credit Note Report

![Credit Note Report: Screen](screenshots/reports/credit_note_report.png)

![Credit Note Report: Show](screenshots/reports/credit_note_report_show.png)

**Page purpose:** This page allows users to search for and view credit note records based on branch and date range.

**Route:** `/reports/otherReports/creditNoteReport`

<!-- manual-meta: {"module": "Reports", "page": "Credit Note Report", "task": "Search Credit Note Records", "action": "search", "roles": [], "route": "/reports/otherReports/creditNoteReport", "screenshots": ["screenshots/reports/credit_note_report.png", "screenshots/reports/credit_note_report_show.png"], "keywords": ["credit note", "report", "invoice"], "task_order": 1} -->
#### Task: Search Credit Note Records

**Purpose:** To generate a list of credit note transactions for audit or review.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Authorized access to reports

**Steps:**
1. Select 'Branch Name' from the dropdown.
2. Select 'From Date'.
3. Select 'To Date'.
4. Click 'View'.

**Fields and controls:**
* **Branch Name:** The branch associated with the credit note.
* **From Date:** The start of the search period.
* **To Date:** The end of the search period.

**Expected result:** A table populated with SL, Branch Name, Partner, Invoice, Fiscal Year, and Transaction Date will appear.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, report, invoice

### Page: Debit Note Report

![Debit Note Report: Screen](screenshots/reports/debit_note_report.png)

![Debit Note Report: Show](screenshots/reports/debit_note_report_show.png)

**Page purpose:** This page provides a search interface to list debit note transactions for specific branches and periods.

**Route:** `/reports/otherReports/debitNoteReport`

<!-- manual-meta: {"module": "Reports", "page": "Debit Note Report", "task": "View Debit Note Report", "action": "search", "roles": [], "route": "/reports/otherReports/debitNoteReport", "screenshots": ["screenshots/reports/debit_note_report.png", "screenshots/reports/debit_note_report_show.png"], "keywords": ["debit note", "report", "transaction"], "task_order": 1} -->
#### Task: View Debit Note Report

**Purpose:** To list debit note entries for a specified time frame.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is logged in

**Steps:**
1. Choose a 'Branch Name'.
2. Set the 'From Date' and 'To Date'.
3. Click 'View'.

**Fields and controls:**
* **Branch Name:** The branch to search.
* **From Date:** Start date for filtering records.
* **To Date:** End date for filtering records.

**Expected result:** Displays a table with debit note transaction details.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, report, transaction

### Page: Document Verification System (DVS)

![Doc Verification System Dvs: Screen](screenshots/reports/doc_verification_system_dvs.png)

**Page purpose:** This page is used for the verification of documents.

**Route:** `/reports/otherReports/docVerificationSystem(DVS)`

<!-- manual-meta: {"module": "Reports", "page": "Document Verification System (DVS)", "task": "Verify Documents", "action": "view", "roles": [], "route": "/reports/otherReports/docVerificationSystem(DVS)", "screenshots": ["screenshots/reports/doc_verification_system_dvs.png"], "keywords": ["dvs", "verification", "document"], "task_order": 1} -->
#### Task: Verify Documents

**Purpose:** To access the document verification system interface.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has permission to access DVS

**Steps:**
1. Navigate to the Reports module.
2. Select 'Doc Verification System (DVS)'.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The DVS interface loads for document entry or searching.

**Warnings:**
* No specific warning was identified

**Search keywords:** dvs, verification, document

### Page: HSCode Wise Sales & Vat Report

![Hscode Wise Sales Vat: Screen](screenshots/reports/hscode_wise_sales_vat.png)

![Hscode Wise Sales Vat: Show](screenshots/reports/hscode_wise_sales_vat_show.png)

**Page purpose:** This page allows users to view sales and VAT information categorized by HS Code for a specific time range.

**Route:** `/reports/otherReports/hsCodeVatSummary`

<!-- manual-meta: {"module": "Reports", "page": "HSCode Wise Sales & Vat Report", "task": "Filter HSCode Sales Report", "action": "filter", "roles": [], "route": "/reports/otherReports/hsCodeVatSummary", "screenshots": ["screenshots/reports/hscode_wise_sales_vat.png", "screenshots/reports/hscode_wise_sales_vat_show.png"], "keywords": ["hscode", "vat", "sales", "report"], "task_order": 1} -->
#### Task: Filter HSCode Sales Report

**Purpose:** To generate a report showing sales quantity, value, and VAT per HS Code.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data exists for selected date range

**Steps:**
1. Select the 'From Date'.
2. Select the 'To Date'.
3. Click 'View'.

**Fields and controls:**
* **From Date:** Start date.
* **To Date:** End date.

**Expected result:** A table displaying columns including HS Code, Item Name, Sales Value, Sales VAT, and Total VAT.

**Warnings:**
* If no data is found, the system will display a notification message.

**Search keywords:** hscode, vat, sales, report

### Page: Inventory Reconciliation

![Inventory Reconciliation: Screen](screenshots/reports/inventory_reconciliation.png)

**Page purpose:** This page facilitates the generation of inventory reports based on specific view types and dates.

**Route:** `/reports/otherReports/inventoryReport`

<!-- manual-meta: {"module": "Reports", "page": "Inventory Reconciliation", "task": "Generate Inventory Report", "action": "view", "roles": [], "route": "/reports/otherReports/inventoryReport", "screenshots": ["screenshots/reports/inventory_reconciliation.png"], "keywords": ["inventory", "reconciliation", "stock", "report"], "task_order": 1} -->
#### Task: Generate Inventory Report

**Purpose:** To compare or review inventory levels.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* System has data to reconcile

**Steps:**
1. Select 'View Type'.
2. Enter 'From Date'.
3. Enter 'To Date'.
4. Click 'View'.

**Fields and controls:**
* **View Type:** Determines the mode of the report output.
* **From Date:** Reporting start date.
* **To Date:** Reporting end date.

**Expected result:** The reconciliation report will be displayed in the interface.

**Warnings:**
* No specific warning was identified

**Search keywords:** inventory, reconciliation, stock, report

### Page: Material Issue Report

![Material Issue Report: Screen](screenshots/reports/material_issue_report.png)

**Page purpose:** This page allows users to view reports detailing material issue transactions by branch and sorting criteria.

**Route:** `/reports/otherReports/materialIssueReport`

<!-- manual-meta: {"module": "Reports", "page": "Material Issue Report", "task": "View Material Issue Details", "action": "view", "roles": [], "route": "/reports/otherReports/materialIssueReport", "screenshots": ["screenshots/reports/material_issue_report.png"], "keywords": ["material", "issue", "stock", "report"], "task_order": 1} -->
#### Task: View Material Issue Details

**Purpose:** To track materials issued from inventory for specific dates.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Valid branch selection

**Steps:**
1. Select the 'Branch'.
2. Select 'Sort By' criteria.
3. Select 'From Date'.
4. Select 'To Date'.
5. Click 'View'.

**Fields and controls:**
* **Branch:** Branch from which the material was issued.
* **Sort By:** Sorting preference for the report results.

**Expected result:** Displays a list of material issue records.

**Warnings:**
* No specific warning was identified

**Search keywords:** material, issue, stock, report

### Page: MIS Report

![Mis Report: Screen](screenshots/reports/mis_report.png)

**Page purpose:** Central dashboard or list for accessing various Management Information System (MIS) reports.

**Route:** `/reports/otherReports`

<!-- manual-meta: {"module": "Reports", "page": "MIS Report", "task": "View MIS Reports", "action": "view", "roles": [], "route": "/reports/otherReports", "screenshots": ["screenshots/reports/mis_report.png"], "keywords": ["reports", "MIS", "dashboard"], "task_order": 1} -->
#### Task: View MIS Reports

**Purpose:** Access specific management reports from the system.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Log in to the system
* Navigate to the Reports module

**Steps:**
1. Click on 'REPORTS' in the side menu
2. Select 'MIS Report' from the dropdown
3. Click on any report name (e.g., 'Purchase Report', 'Sales Report') to view its details

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The selected report screen will open.

**Warnings:**
* No specific warning was identified

**Search keywords:** reports, MIS, dashboard

### Page: Mushak 4.3 (Price Declaration)

![Mushak 4 3 Price Declaration: Screen](screenshots/reports/mushak_4_3_price_declaration.png)

**Page purpose:** List of price declarations for items, including tax and price details.

**Route:** `/reports/mushakForms/mushak4.3`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.3 (Price Declaration)", "task": "Search Items", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak4.3", "screenshots": ["screenshots/reports/mushak_4_3_price_declaration.png"], "keywords": ["price declaration", "mushak 4.3"], "task_order": 1} -->
#### Task: Search Items

**Purpose:** Find specific item price declarations.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Type the item name into the 'Item Name Search' field
2. Observe the filtered result in the table

**Fields and controls:**
* **Item Name Search:** Filter by item name.

**Expected result:** The table updates to show matching price declarations.

**Warnings:**
* No specific warning was identified

**Search keywords:** price declaration, mushak 4.3

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.3 (Price Declaration)", "task": "Adjust Pagination", "action": "configure", "roles": [], "route": "/reports/mushakForms/mushak4.3", "screenshots": ["screenshots/reports/mushak_4_3_price_declaration.png"], "keywords": ["pagination", "view"], "task_order": 2} -->
#### Task: Adjust Pagination

**Purpose:** Control how many records are shown per page.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Click on the 'rows per page' dropdown
2. Select the desired number of rows (e.g., 15, 25, 50)

**Fields and controls:**
* **rows per page:** Dropdown to select display count.

**Expected result:** The table refreshes to display the selected number of rows.

**Warnings:**
* No specific warning was identified

**Search keywords:** pagination, view

### Page: Mushak 4.4 (Item Destroy)

![Mushak 4 4 Item Destroy: Screen](screenshots/reports/mushak_4_4_item_destroy.png)

**Page purpose:** Report screen for destroyed items.

**Route:** `/reports/mushakForms/mushak4.4`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.4 (Item Destroy)", "task": "Filter Destroyed Item Records", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak4.4", "screenshots": ["screenshots/reports/mushak_4_4_item_destroy.png"], "keywords": ["item destroy", "mushak 4.4"], "task_order": 1} -->
#### Task: Filter Destroyed Item Records

**Purpose:** View item destruction records for a specific date range or category.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Select Branch, Item Type, and Item Name from the respective dropdowns
2. Set the 'From Date' and 'To Date'
3. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the branch.
* **Item Type:** Select the item category.
* **Item Name:** Select the specific item.
* **From Date:** Filter start date.
* **To Date:** Filter end date.

**Expected result:** The system displays the records matching the chosen filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** item destroy, mushak 4.4

### Page: Mushak 4.5 (Accident Destroy)

![Mushak 4 5 Accident Destroy: Screen](screenshots/reports/mushak_4_5_accident_destroy.png)

**Page purpose:** Report screen for items destroyed due to accidents.

**Route:** `/reports/mushakForms/mushak4.5`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.5 (Accident Destroy)", "task": "Filter Accident Destroy Records", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak4.5", "screenshots": ["screenshots/reports/mushak_4_5_accident_destroy.png"], "keywords": ["accident destroy", "mushak 4.5"], "task_order": 1} -->
#### Task: Filter Accident Destroy Records

**Purpose:** Search for specific accident destruction reports.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Input criteria in Branch, Item Type, and Item Name fields
2. Set the date range using 'From Date' and 'To Date'
3. Click the 'View' button

**Fields and controls:**
* **Branch:** Select a branch.
* **Item Type:** Select item type.
* **Item Name:** Select an item.
* **From Date:** Start date for report.
* **To Date:** End date for report.

**Expected result:** The system populates results based on your criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** accident destroy, mushak 4.5

### Page: Mushak 4.6 (Waste Disposal)

![Mushak 4 6 Waste Disposal: Screen](screenshots/reports/mushak_4_6_waste_disposal.png)

**Page purpose:** List of waste disposal records with quantities and dates.

**Route:** `/reports/mushakForms/mushak4.6`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.6 (Waste Disposal)", "task": "View Waste Disposal History", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak4.6", "screenshots": ["screenshots/reports/mushak_4_6_waste_disposal.png"], "keywords": ["waste disposal", "mushak 4.6"], "task_order": 1} -->
#### Task: View Waste Disposal History

**Purpose:** Review historical waste disposal entries.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the page to load the default table of waste disposal records
2. Use the pagination dropdown to adjust how many rows appear

**Fields and controls:**
* **rows per page:** Adjust list size.

**Expected result:** The disposal table displays the requested number of entries.

**Warnings:**
* No specific warning was identified

**Search keywords:** waste disposal, mushak 4.6

### Page: Mushak 6.10 (P&S +2 Lakh)

![Mushak 6 10 P S 2 Lakh: Screen](screenshots/reports/mushak_6_10_p_s_2_lakh.png)

![Mushak 6 10 P S 2 Lakh: Show](screenshots/reports/mushak_6_10_p_s_2_lakh_show.png)

**Page purpose:** Report of Purchase and Sales records exceeding 2 Lakh.

**Route:** `/reports/mushakForms/mushak6.10`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.10 (P&S +2 Lakh)", "task": "Generate P&S +2 Lakh Report", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.10", "screenshots": ["screenshots/reports/mushak_6_10_p_s_2_lakh.png", "screenshots/reports/mushak_6_10_p_s_2_lakh_show.png"], "keywords": ["p&s 2 lakh", "mushak 6.10"], "task_order": 1} -->
#### Task: Generate P&S +2 Lakh Report

**Purpose:** View transactional data for values over 2 Lakh.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Select the 'Branch' from the dropdown
2. Select the 'From Date' and 'To Date'
3. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the business unit.
* **From Date:** Filter starting date.
* **To Date:** Filter ending date.

**Expected result:** Report data is loaded or a 'not available' message is displayed.

**Warnings:**
* If the report is empty, the system may show a 'Purchase/Sales information not available' alert.

**Search keywords:** p&s 2 lakh, mushak 6.10

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.10 (P&S +2 Lakh)", "task": "Export Report to Excel", "action": "export", "roles": [], "route": "/reports/mushakForms/mushak6.10", "screenshots": ["screenshots/reports/mushak_6_10_p_s_2_lakh.png", "screenshots/reports/mushak_6_10_p_s_2_lakh_show.png"], "keywords": ["export", "excel", "report"], "task_order": 2} -->
#### Task: Export Report to Excel

**Purpose:** Download the generated report in Excel format.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Report data must be generated

**Steps:**
1. Click the 'Excel' button at the top right

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** An Excel file will be downloaded to your device.

**Warnings:**
* No specific warning was identified

**Search keywords:** export, excel, report

### Page: Mushak 6.1 (Purchase Register)

![Mushak 6 1 Purchase Register: Screen](screenshots/reports/mushak_6_1_purchase_register.png)

**Page purpose:** Comprehensive register for all purchase transactions.

**Route:** `/reports/mushakForms/mushak6.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.1 (Purchase Register)", "task": "View Purchase Register", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.1", "screenshots": ["screenshots/reports/mushak_6_1_purchase_register.png"], "keywords": ["purchase register", "mushak 6.1"], "task_order": 1} -->
#### Task: View Purchase Register

**Purpose:** Examine purchase records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Select 'Item Type', 'Item', and 'Branch' from dropdowns
2. Select the 'From Date' and 'To Date'
3. Choose a display format (Bangla or English)
4. Click 'View'

**Fields and controls:**
* **Item Type:** Type of item purchased.
* **Item:** Specific item name.
* **Branch:** Relevant branch.
* **Bangla format / English format:** Select language output.

**Expected result:** The purchase register will be displayed based on the filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** purchase register, mushak 6.1

### Page: Mushak 6.2.1 (P&S Register)

![Mushak 6 2 1 P S Register: Screen](screenshots/reports/mushak_6_2_1_p_s_register.png)

**Page purpose:** Combined register for Purchase and Sales transactions.

**Route:** `/reports/mushakForms/mushak6-2-1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.2.1 (P&S Register)", "task": "Filter P&S Register", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6-2-1", "screenshots": ["screenshots/reports/mushak_6_2_1_p_s_register.png"], "keywords": ["p&s register", "mushak 6.2.1"], "task_order": 1} -->
#### Task: Filter P&S Register

**Purpose:** Search for specific purchase and sales register data.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Select Item Type, Item, and Branch
2. Set the 'From Date' and 'To Date'
3. Click 'View'

**Fields and controls:**
* **Item Type:** Category for filtering.
* **Item Name:** Specific product.
* **Branch:** Filter by branch.
* **From Date:** Filter period start.
* **To Date:** Filter period end.

**Expected result:** The screen displays the filtered register records.

**Warnings:**
* No specific warning was identified

**Search keywords:** p&s register, mushak 6.2.1

### Page: Mushak 6.2 (Sales Register)

![Mushak 6 2 Sales Register: Screen](screenshots/reports/mushak_6_2_sales_register.png)

**Page purpose:** Used to view the sales register for specific items, branches, and date ranges.

**Route:** `/reports/mushakForms/mushak6.2`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.2 (Sales Register)", "task": "Generate Sales Register report", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.2", "screenshots": ["screenshots/reports/mushak_6_2_sales_register.png"], "keywords": ["sales register", "Mushak 6.2"], "task_order": 1} -->
#### Task: Generate Sales Register report

**Purpose:** To view a summary of sales transactions for a chosen period and filter settings.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Reports module

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.2 (Sales Register)
2. Select Item Type and Item from the dropdowns
3. Select the Branch
4. Pick the From Date and To Date using the date picker
5. Select either 'Bangla format' or 'English format'
6. Click the 'View' button

**Fields and controls:**
* **Item Type:** Category of items to include in the report.
* **Item:** Specific item name.
* **Branch:** Organizational branch for the report.
* **From Date:** Start date for the report period.
* **To Date:** End date for the report period.
* **Format radio buttons:** Select between Bangla or English language format.

**Expected result:** The sales register report is displayed based on the selected criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales register, Mushak 6.2

### Page: Mushak 6.3 (Sales Invoice)

![Mushak 6 3 Sales Invoice: Screen](screenshots/reports/mushak_6_3_sales_invoice.png)

![Mushak 6 3 Sales Invoice: Show](screenshots/reports/mushak_6_3_sales_invoice_show.png)

**Page purpose:** Used to search and view sales invoices.

**Route:** `/reports/mushakForms/mushak6.3`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.3 (Sales Invoice)", "task": "Search for Sales Invoices", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.3", "screenshots": ["screenshots/reports/mushak_6_3_sales_invoice.png", "screenshots/reports/mushak_6_3_sales_invoice_show.png"], "keywords": ["sales invoice", "search invoice"], "task_order": 1} -->
#### Task: Search for Sales Invoices

**Purpose:** To quickly locate a specific sales invoice using identifiers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Invoices must exist for the selected branch

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.3 (Sales Invoice)
2. Select the Branch
3. Enter the BOE, BIN, or Invoice Number in the search field
4. Click the search icon

**Fields and controls:**
* **Select Branch:** The branch to pull invoices from.
* **Enter From Date:** Start date of the search range.
* **Enter To Date:** End date of the search range.
* **BOE, BIN, Inv No Search:** Input field for invoice, bill of entry, or tax ID search.

**Expected result:** Invoices matching the criteria are listed in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales invoice, search invoice

### Page: Mushak 6.4 (Issue MFG.)

![Mushak 6 4 Issue Mfg: Screen](screenshots/reports/mushak_6_4_issue_mfg.png)

![Mushak 6 4 Issue Mfg: Show](screenshots/reports/mushak_6_4_issue_mfg_show.png)

**Page purpose:** Used to monitor contract manufacturing issue and receive transactions.

**Route:** `/reports/mushakForms/mushak6.4`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.4 (Issue MFG.)", "task": "View Contract Manufacturing Reports", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.4", "screenshots": ["screenshots/reports/mushak_6_4_issue_mfg.png", "screenshots/reports/mushak_6_4_issue_mfg_show.png"], "keywords": ["issue mfg", "contract manufacturing"], "task_order": 1} -->
#### Task: View Contract Manufacturing Reports

**Purpose:** To track raw materials issued or received for contract manufacturing.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to Reports module

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.4 (Issue MFG.)
2. Select between 'CONTRACT MANUFACTURING ISSUE' or 'CONTRACT MANUFACTURING RECEIVE' tabs
3. Select the Branch
4. Set the date range
5. Select the Issue Type
6. Click the 'View' button

**Fields and controls:**
* **Branch:** The branch to view.
* **From Date:** Start date.
* **To Date:** End date.
* **Issue Type:** The category of issued materials.

**Expected result:** A table showing challans, suppliers, and quantities appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** issue mfg, contract manufacturing

### Page: Mushak 6.5 (Stock Transfer)

![Mushak 6 5 Stock Transfer: Screen](screenshots/reports/mushak_6_5_stock_transfer.png)

![Mushak 6 5 Stock Transfer: Show](screenshots/reports/mushak_6_5_stock_transfer_show.png)

**Page purpose:** Used to view records of stock transfers between branches.

**Route:** `/reports/mushakForms/mushak6.5`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.5 (Stock Transfer)", "task": "View Stock Transfer list", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.5", "screenshots": ["screenshots/reports/mushak_6_5_stock_transfer.png", "screenshots/reports/mushak_6_5_stock_transfer_show.png"], "keywords": ["stock transfer", "transfer history"], "task_order": 1} -->
#### Task: View Stock Transfer list

**Purpose:** To verify the history of stock transferred from a selected branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Transfers must have been performed

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.5 (Stock Transfer)
2. Select Branch Name
3. Select Item Type
4. Click 'View'

**Fields and controls:**
* **Branch Name:** Originating branch of the transfer.
* **Item Type:** The type of items transferred.

**Expected result:** A list of transfers with details like transfer number, destination, and vehicle number is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** stock transfer, transfer history

### Page: Mushak 6.6 (VDS Certificate)

![Mushak 6 6 Vds Certificate: Screen](screenshots/reports/mushak_6_6_vds_certificate.png)

![Mushak 6 6 Vds Certificate: Show](screenshots/reports/mushak_6_6_vds_certificate_show.png)

**Page purpose:** Used to track and issue VDS certificates.

**Route:** `/reports/mushakForms/mushak6.6`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.6 (VDS Certificate)", "task": "Filter VDS Certificates", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.6", "screenshots": ["screenshots/reports/mushak_6_6_vds_certificate.png", "screenshots/reports/mushak_6_6_vds_certificate_show.png"], "keywords": ["vds", "certificate", "tax deduction"], "task_order": 1} -->
#### Task: Filter VDS Certificates

**Purpose:** To list VDS certificates based on their status.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to Reports module

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.6 (VDS Certificate)
2. Select the Report Type
3. Select the Branch
4. Select a status (All, Pending, or Complete)
5. Click 'View'

**Fields and controls:**
* **Select Report Type:** The specific certificate report type.
* **Select Branch:** Branch to query.
* **Status radio buttons:** Filters for certificate completion status.

**Expected result:** The report table is updated to show certificates matching the selected status.

**Warnings:**
* No specific warning was identified

**Search keywords:** vds, certificate, tax deduction

### Page: Mushak 6.7 (Credit Note)

![Mushak 6 7 Credit Note: Screen](screenshots/reports/mushak_6_7_credit_note.png)

**Page purpose:** Used to view sales credit notes.

**Route:** `/reports/mushakForms/mushak6.7`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.7 (Credit Note)", "task": "View Credit Notes", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.7", "screenshots": ["screenshots/reports/mushak_6_7_credit_note.png"], "keywords": ["credit note", "sales return"], "task_order": 1} -->
#### Task: View Credit Notes

**Purpose:** To list generated credit notes for customer sales.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Sales invoices must exist

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.7 (Credit Note)
2. Select the Branch
3. Set the Date range
4. Click 'View'

**Fields and controls:**
* **Branch:** Selected business branch.
* **Form Date:** Start date for credit notes.
* **To Date:** End date for credit notes.

**Expected result:** Table displays existing credit notes.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, sales return

### Page: Mushak 6.8 (Debit Note)

![Mushak 6 8 Debit Note: Screen](screenshots/reports/mushak_6_8_debit_note.png)

![Mushak 6 8 Debit Note: Show](screenshots/reports/mushak_6_8_debit_note_show.png)

**Page purpose:** Used to view purchase debit notes.

**Route:** `/reports/mushakForms/mushak6.8`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.8 (Debit Note)", "task": "View Debit Notes", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.8", "screenshots": ["screenshots/reports/mushak_6_8_debit_note.png", "screenshots/reports/mushak_6_8_debit_note_show.png"], "keywords": ["debit note", "purchase return"], "task_order": 1} -->
#### Task: View Debit Notes

**Purpose:** To list generated debit notes for purchase invoices.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Purchase invoices must exist

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.8 (Debit Note)
2. Select the Branch
3. Set the Date range
4. Click 'View'

**Fields and controls:**
* **Branch Name:** Selected business branch.
* **Form Date:** Start date.
* **To Date:** End date.

**Expected result:** Table displays existing debit notes.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, purchase return

### Page: Mushak 9.1 (VAT Return)

![Mushak 9 1 Vat Return: Screen](screenshots/reports/mushak_9_1_vat_return.png)

![Mushak 9 1 Vat Return: Show](screenshots/reports/mushak_9_1_vat_return_show.png)

**Page purpose:** Used to prepare, view, and post VAT returns for a specific month.

**Route:** `/reports/mushakForms/mushak9.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 9.1 (VAT Return)", "task": "Generate VAT Return", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak9.1", "screenshots": ["screenshots/reports/mushak_9_1_vat_return.png", "screenshots/reports/mushak_9_1_vat_return_show.png"], "keywords": ["vat return", "mushak 9.1", "tax return"], "task_order": 1} -->
#### Task: Generate VAT Return

**Purpose:** To view the compiled VAT return form for the selected month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Transactions for the period are complete

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 9.1 (VAT Return)
2. Select the Month
3. Click the 'View' button

**Fields and controls:**
* **Month:** Target month for the VAT return.

**Expected result:** The full VAT return form is rendered.

**Warnings:**
* No specific warning was identified

**Search keywords:** vat return, mushak 9.1, tax return

### Page: Mushak Forms

![Mushak Forms: Screen](screenshots/reports/mushak_forms.png)

**Page purpose:** This page provides access to various regulatory Mushak forms and reports for VAT compliance.

**Route:** `/reports/mushakForms`

<!-- manual-meta: {"module": "Reports", "page": "Mushak Forms", "task": "Access Regulatory Mushak Forms", "action": "view", "roles": [], "route": "/reports/mushakForms", "screenshots": ["screenshots/reports/mushak_forms.png"], "keywords": ["VAT", "statutory report", "Mushak"], "task_order": 1} -->
#### Task: Access Regulatory Mushak Forms

**Purpose:** To view or generate specific statutory VAT documents.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* The user must be logged into the system.
* The user must have navigation access to the Reports module.

**Steps:**
1. Navigate to the Reports module in the sidebar.
2. Select 'Mushak Forms'.
3. Choose a specific form (e.g., Mushak 4.3, 6.1, or 9.1) from the provided list.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The selected Mushak report or form generation interface is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** VAT, statutory report, Mushak

### Page: Partner Vs Stock Report

![Partner Vs Stock: Screen](screenshots/reports/partner_vs_stock.png)

**Page purpose:** This report displays a comparison of stock levels associated with specific partners.

**Route:** `/reports/otherReports/partnerVsStock`

<!-- manual-meta: {"module": "Reports", "page": "Partner Vs Stock Report", "task": "Filter Partner vs Stock Data", "action": "filter", "roles": [], "route": "/reports/otherReports/partnerVsStock", "screenshots": ["screenshots/reports/partner_vs_stock.png"], "keywords": ["inventory", "stock report", "customer stock"], "task_order": 1} -->
#### Task: Filter Partner vs Stock Data

**Purpose:** To view stock inventory levels filtered by specific branch, customer, or item.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be on the Partner Vs Stock report page.

**Steps:**
1. Select a branch from the 'Branch' dropdown.
2. Select or search for a customer name in the 'Customer Name' field.
3. Select an item from the 'Item' dropdown.
4. Click the 'View' button to display the results.

**Fields and controls:**
* **Branch:** Select the location branch.
* **Customer Name:** Filter by specific customer.
* **Item:** Filter by specific inventory item.

**Expected result:** The table below populates with SL, Item Name, Item Code, UoM Name, Declare Price, and Stock values based on the filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** inventory, stock report, customer stock

### Page: Payment Method Wise Report

![Payment Method Wise Report: Screen](screenshots/reports/payment_method_wise_report.png)

![Payment Method Wise Report: Show](screenshots/reports/payment_method_wise_report_show.png)

**Page purpose:** This report tracks sales transactions grouped by their respective payment methods within a defined date range.

**Route:** `/reports/otherReports/paymentMethodWiseReport`

<!-- manual-meta: {"module": "Reports", "page": "Payment Method Wise Report", "task": "View Payment Method Wise Report", "action": "view", "roles": [], "route": "/reports/otherReports/paymentMethodWiseReport", "screenshots": ["screenshots/reports/payment_method_wise_report.png", "screenshots/reports/payment_method_wise_report_show.png"], "keywords": ["sales report", "payment tracking", "financial report"], "task_order": 1} -->
#### Task: View Payment Method Wise Report

**Purpose:** To analyze sales based on payment methods used over a specific time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the MIS Report section.

**Steps:**
1. Select the Item Type (e.g., Sales).
2. Select the Payment Method Type (e.g., All).
3. Input the 'From Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Item Type:** The category of transaction to filter.
* **Payment Method Type:** Specific payment mode (e.g., Cash, Bank).
* **Enter From Date:** Start date for report range.
* **Enter To Date:** End date for report range.

**Expected result:** The system generates the payment method report for the selected criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales report, payment tracking, financial report

### Page: Production Report

![Production Report: Screen](screenshots/reports/production_report.png)

**Page purpose:** This report provides a breakdown of production activity by branch and date.

**Route:** `/reports/otherReports/productionReport`

<!-- manual-meta: {"module": "Reports", "page": "Production Report", "task": "Generate Production Report", "action": "view", "roles": [], "route": "/reports/otherReports/productionReport", "screenshots": ["screenshots/reports/production_report.png"], "keywords": ["production output", "manufacturing report"], "task_order": 1} -->
#### Task: Generate Production Report

**Purpose:** To monitor production output over a specific period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Select the 'Branch'.
2. Select the 'Sort By' preference.
3. Select 'From Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Branch:** The site of production.
* **Sort By:** Criteria for ordering data.

**Expected result:** A detailed production report is displayed based on inputs.

**Warnings:**
* No specific warning was identified

**Search keywords:** production output, manufacturing report

### Page: Purchase Report

![Purchase Report: Screen](screenshots/reports/purchase_report.png)

![Purchase Report: Show](screenshots/reports/purchase_report_show.png)

**Page purpose:** A comprehensive view of purchase transactions.

**Route:** `/reports/otherReports/purchaseReport`

<!-- manual-meta: {"module": "Reports", "page": "Purchase Report", "task": "Filter Purchase Transactions", "action": "filter", "roles": [], "route": "/reports/otherReports/purchaseReport", "screenshots": ["screenshots/reports/purchase_report.png", "screenshots/reports/purchase_report_show.png"], "keywords": ["procurement", "purchase history"], "task_order": 1} -->
#### Task: Filter Purchase Transactions

**Purpose:** To view purchase data for specific operational branches and timeframes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Choose a 'Branch'.
2. Select sorting criteria via 'Sort By'.
3. Specify 'From Date' and 'To Date'.
4. Click 'View'.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** Purchase report data is filtered according to user input.

**Warnings:**
* No specific warning was identified

**Search keywords:** procurement, purchase history

### Page: Category Wise Purchase Report

![Purchase Report By Category: Screen](screenshots/reports/purchase_report_by_category.png)

![Purchase Report By Category: Show](screenshots/reports/purchase_report_by_category_show.png)

**Page purpose:** This report displays purchases aggregated by product categories.

**Route:** `/reports/otherReports/purchaseReportByCategory`

<!-- manual-meta: {"module": "Reports", "page": "Category Wise Purchase Report", "task": "View Purchase Data by Category", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseReportByCategory", "screenshots": ["screenshots/reports/purchase_report_by_category.png", "screenshots/reports/purchase_report_by_category_show.png"], "keywords": ["spending analysis", "procurement category"], "task_order": 1} -->
#### Task: View Purchase Data by Category

**Purpose:** To analyze spending or procurement by category types.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Input the 'Enter From Date'.
2. Input the 'Enter To Date'.
3. Click 'View'.

**Fields and controls:**
* **Enter From Date:** Start of report period.
* **Enter To Date:** End of report period.

**Expected result:** A category-wise summary of purchases is rendered.

**Warnings:**
* No specific warning was identified

**Search keywords:** spending analysis, procurement category

### Page: Purchase/Sales Details

![Purchase Sales Details: Screen](screenshots/reports/purchase_sales_details.png)

**Page purpose:** This report allows for deep-dive analysis into specific transaction types within a date range.

**Route:** `/reports/otherReports/purchaseSalesDetails`

<!-- manual-meta: {"module": "Reports", "page": "Purchase/Sales Details", "task": "Generate Detailed Transaction Report", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseSalesDetails", "screenshots": ["screenshots/reports/purchase_sales_details.png"], "keywords": ["transaction log", "sales details", "purchase details"], "task_order": 1} -->
#### Task: Generate Detailed Transaction Report

**Purpose:** To retrieve granular details of either purchases or sales.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Select the 'From Date'.
2. Select the 'To Date'.
3. Choose the transaction type in 'Select Type'.
4. Click 'View'.

**Fields and controls:**
* **Select Type:** Choose between purchase or sales records.

**Expected result:** The page displays the requested transaction details.

**Warnings:**
* No specific warning was identified

**Search keywords:** transaction log, sales details, purchase details

### Page: User Profile

![Reports: Screen](screenshots/reports/reports.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/reports`

<!-- manual-meta: {"module": "Reports", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/reports", "screenshots": ["screenshots/reports/reports.png"], "keywords": ["User Profile", "reports"], "task_order": 1} -->
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

**Search keywords:** User Profile, reports

### Page: Sales & Purchase Compare

![Sales Purchase Compare: Screen](screenshots/reports/sales_purchase_compare.png)

![Sales Purchase Compare: Show](screenshots/reports/sales_purchase_compare_show.png)

**Page purpose:** Used to compare sales and purchase data between different dates.

**Route:** `/reports/otherReports/salesAndPurchaseCompare`

<!-- manual-meta: {"module": "Reports", "page": "Sales & Purchase Compare", "task": "Generate sales and purchase comparison report", "action": "view", "roles": [], "route": "/reports/otherReports/salesAndPurchaseCompare", "screenshots": ["screenshots/reports/sales_purchase_compare.png", "screenshots/reports/sales_purchase_compare_show.png"], "keywords": ["compare", "VAT", "sales", "purchase", "report"], "task_order": 1} -->
#### Task: Generate sales and purchase comparison report

**Purpose:** To compare transaction volumes and VAT between specified dates.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales & Purchase Compare.
2. Select Branch.
3. Select Type.
4. Select 'Based On' option (e.g., Day).
5. Select Purchase Compare (Date) and Sales Compare (Date).
6. Click 'View'.

**Fields and controls:**
* **Branch:** Branch selector.
* **Type:** Report type selector.
* **Based On:** Filtering basis (e.g., Day).
* **Purchase Compare (Date):** Start date for purchase records.
* **Sales Compare (Date):** Start date for sales records.

**Expected result:** View the comparison table containing SL, Date, Branch Name, Purchase Compare details, and Sales Compare details.

**Warnings:**
* No specific warning was identified

**Search keywords:** compare, VAT, sales, purchase, report

### Page: Sales Report

![Sales Report: Screen](screenshots/reports/sales_report.png)

**Page purpose:** Provides a detailed report of sales transactions.

**Route:** `/reports/otherReports/salesReport`

<!-- manual-meta: {"module": "Reports", "page": "Sales Report", "task": "View sales report", "action": "view", "roles": [], "route": "/reports/otherReports/salesReport", "screenshots": ["screenshots/reports/sales_report.png"], "keywords": ["sales", "invoices", "transactions"], "task_order": 1} -->
#### Task: View sales report

**Purpose:** To retrieve and review sales transactions within a specific date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Report.
2. Select the Branch.
3. Choose sorting criteria in 'Sort By'.
4. Enter 'From Date' and 'To Date'.
5. Click 'View'.

**Fields and controls:**
* **Branch:** Select the company branch.
* **Sort By:** Sorting criteria for the list.
* **From Date:** Start date range.
* **To Date:** End date range.

**Expected result:** Displays a filtered list of sales records based on selected parameters.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoices, transactions

### Page: Sales Report by Category

![Sales Report By Category: Screen](screenshots/reports/sales_report_by_category.png)

![Sales Report By Category: Show](screenshots/reports/sales_report_by_category_show.png)

**Page purpose:** Displays sales data categorized by product or service types.

**Route:** `/reports/otherReports/salesReportByCategory`

<!-- manual-meta: {"module": "Reports", "page": "Sales Report by Category", "task": "View category-wise sales", "action": "view", "roles": [], "route": "/reports/otherReports/salesReportByCategory", "screenshots": ["screenshots/reports/sales_report_by_category.png", "screenshots/reports/sales_report_by_category_show.png"], "keywords": ["category", "sales", "report"], "task_order": 1} -->
#### Task: View category-wise sales

**Purpose:** To analyze sales performance segmented by categories.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Report by Category.
2. Enter 'Enter From Date'.
3. Enter 'Enter To Date'.
4. Click 'View'.

**Fields and controls:**
* **Enter From Date:** Start date of the sales report.
* **Enter To Date:** End date of the sales report.

**Expected result:** A list of sales figures grouped by category.

**Warnings:**
* No specific warning was identified

**Search keywords:** category, sales, report

### Page: Sales & Stock Summary

![Sales Stock Summary: Screen](screenshots/reports/sales_stock_summary.png)

![Sales Stock Summary: Show](screenshots/reports/sales_stock_summary_show.png)

**Page purpose:** Provides a comprehensive view of stock movements versus sales activity.

**Route:** `/reports/otherReports/SalesStockSummary`

<!-- manual-meta: {"module": "Reports", "page": "Sales & Stock Summary", "task": "Generate sales and stock summary report", "action": "view", "roles": [], "route": "/reports/otherReports/SalesStockSummary", "screenshots": ["screenshots/reports/sales_stock_summary.png", "screenshots/reports/sales_stock_summary_show.png"], "keywords": ["inventory", "stock", "sales", "summary"], "task_order": 1} -->
#### Task: Generate sales and stock summary report

**Purpose:** To track inventory, purchase, and sales details for a given month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales & Stock Summary.
2. Select the Month.
3. Click 'View'.

**Fields and controls:**
* **Month:** Calendar month selector.

**Expected result:** Summary table displaying product, purchase, sales, and closing stock information.

**Warnings:**
* No specific warning was identified

**Search keywords:** inventory, stock, sales, summary

### Page: Sales Summary Report

![Sales Summary Report: Screen](screenshots/reports/sales_summary_report.png)

![Sales Summary Report: Show](screenshots/reports/sales_summary_report_show.png)

**Page purpose:** Summarizes sales invoice data by branch and date.

**Route:** `/reports/otherReports/salesSummaryReport`

<!-- manual-meta: {"module": "Reports", "page": "Sales Summary Report", "task": "View sales summary", "action": "view", "roles": [], "route": "/reports/otherReports/salesSummaryReport", "screenshots": ["screenshots/reports/sales_summary_report.png", "screenshots/reports/sales_summary_report_show.png"], "keywords": ["sales", "summary", "invoices"], "task_order": 1} -->
#### Task: View sales summary

**Purpose:** To monitor sales invoices and associated customer details.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Summary Report.
2. Select the 'Select Branch'.
3. Set the 'Enter From Date' and 'Enter To Date'.
4. Click 'View'.

**Fields and controls:**
* **Select Branch:** Filter by business unit.
* **Enter From Date:** Beginning of the date range.
* **Enter To Date:** End of the date range.

**Expected result:** Displays a summary list of sales transactions.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, summary, invoices

### Page: Stock Reconcile Report

![Stock Reconsile Report: Screen](screenshots/reports/stock_reconsile_report.png)

**Page purpose:** Used for verifying stock levels and performing reconciliation.

**Route:** `/reports/otherReports/stockReconsileReport`

<!-- manual-meta: {"module": "Reports", "page": "Stock Reconcile Report", "task": "Run stock reconciliation report", "action": "view", "roles": [], "route": "/reports/otherReports/stockReconsileReport", "screenshots": ["screenshots/reports/stock_reconsile_report.png"], "keywords": ["reconcile", "stock", "audit"], "task_order": 1} -->
#### Task: Run stock reconciliation report

**Purpose:** To compare physical stock against system records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Stock Reconsile Report.
2. Select the Branch.
3. Select the From Date.
4. Click 'View'.

**Fields and controls:**
* **Branch:** Branch selector.
* **From Date:** Start date for reconciliation.

**Expected result:** The screen will display current reconciliations for the selected criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** reconcile, stock, audit

### Page: Stock Register

![Stock Register: Screen](screenshots/reports/stock_register.png)

![Stock Register: Show](screenshots/reports/stock_register_show.png)

**Page purpose:** Detailed ledger of stock movements including openings, receipts, and issues.

**Route:** `/reports/otherReports/stockRegister`

<!-- manual-meta: {"module": "Reports", "page": "Stock Register", "task": "View stock register report", "action": "view", "roles": [], "route": "/reports/otherReports/stockRegister", "screenshots": ["screenshots/reports/stock_register.png", "screenshots/reports/stock_register_show.png"], "keywords": ["ledger", "stock", "quantity", "movements"], "task_order": 1} -->
#### Task: View stock register report

**Purpose:** To maintain visibility over item-level stock changes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Stock Register.
2. Select Branch.
3. Select Item Type.
4. Select date range using 'Enter From Date' and 'Enter To Date'.
5. Toggle 'Negative Stock' if needed.
6. Click 'View'.

**Fields and controls:**
* **Select Branch:** Filter by branch.
* **Item Type:** Category or type of items.
* **Enter From Date:** Report start date.
* **Enter To Date:** Report end date.
* **Negative Stock:** Checkbox to display items with negative balances.

**Expected result:** Table showing detailed stock quantities, values, and movements.

**Warnings:**
* No specific warning was identified

**Search keywords:** ledger, stock, quantity, movements

### Page: Transaction Log

![Transaction Log: Screen](screenshots/reports/transaction_log.png)

**Page purpose:** Audit trail for system transactions.

**Route:** `/reports/otherReports/auditLog`

<!-- manual-meta: {"module": "Reports", "page": "Transaction Log", "task": "Query transaction logs", "action": "search", "roles": [], "route": "/reports/otherReports/auditLog", "screenshots": ["screenshots/reports/transaction_log.png"], "keywords": ["audit", "log", "transaction", "history"], "task_order": 1} -->
#### Task: Query transaction logs

**Purpose:** To audit and track activities within the system.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Transaction Log.
2. Select 'View Type'.
3. Set 'From Date' and 'To Date'.
4. Click 'View'.

**Fields and controls:**
* **View Type:** Category of log to display.
* **From Date:** Log start date.
* **To Date:** Log end date.

**Expected result:** List of system transactions corresponding to the selected dates.

**Warnings:**
* No specific warning was identified

**Search keywords:** audit, log, transaction, history

### Page: Transit Report

![Transit Report: Screen](screenshots/reports/transit_report.png)

![Transit Report: Show](screenshots/reports/transit_report_show.png)

**Page purpose:** This page provides a report on items currently in transit between branches, allowing for monitoring of transfer details and quantities.

**Route:** `/reports/otherReports/transitReport`

<!-- manual-meta: {"module": "Reports", "page": "Transit Report", "task": "View Transit Report", "action": "view", "roles": [], "route": "/reports/otherReports/transitReport", "screenshots": ["screenshots/reports/transit_report.png", "screenshots/reports/transit_report_show.png"], "keywords": ["transit", "stock transfer", "branch report"], "task_order": 1} -->
#### Task: View Transit Report

**Purpose:** To monitor stock transfer statuses between different branches within a selected date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module.

**Steps:**
1. Navigate to Reports > MIS Report > Transit Report.
2. Select the Branch from the dropdown menu.
3. Select the Item Type from the dropdown menu.
4. Select the From Date using the calendar picker.
5. Select the To Date using the calendar picker.
6. Click the View button.

**Fields and controls:**
* **Branch:** The specific branch from which the transit report is generated.
* **Item Type:** The category or type of item being tracked in transit.
* **From Date:** The start date for the reporting period.
* **To Date:** The end date for the reporting period.

**Expected result:** The system displays a table containing SL, Branch Name, Transfer Date, Transfer No, From Branch, From Address, To Branch, To Address, Item Name, Transfer Qty, Receive Qty, Pending Qty, and Narration. If no records exist, a 'Data Not Found' message is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** transit, stock transfer, branch report

### Page: Treasury Deposit Report

![Treasury Deposit Report: Screen](screenshots/reports/treasury_deposit_report.png)

![Treasury Deposit Report: Show](screenshots/reports/treasury_deposit_report_show.png)

**Page purpose:** This page provides a view of treasury deposit transactions within a specified date range.

**Route:** `/reports/otherReports/treasuryDepositReport`

<!-- manual-meta: {"module": "Reports", "page": "Treasury Deposit Report", "task": "View Treasury Deposit Report", "action": "view", "roles": [], "route": "/reports/otherReports/treasuryDepositReport", "screenshots": ["screenshots/reports/treasury_deposit_report.png", "screenshots/reports/treasury_deposit_report_show.png"], "keywords": ["treasury", "deposit", "financial report"], "task_order": 1} -->
#### Task: View Treasury Deposit Report

**Purpose:** To track and audit treasury deposit records for a specific time frame.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module.

**Steps:**
1. Navigate to Reports > MIS Report > Treasury Deposit Report.
2. Select the From Date using the calendar picker.
3. Select the To Date using the calendar picker.
4. Click the View button.

**Fields and controls:**
* **From Date:** The beginning of the date range for the deposit report.
* **To Date:** The conclusion of the date range for the deposit report.

**Expected result:** The report displays the relevant treasury deposit data for the selected period. If no records are found, a 'Data Not Found' message appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** treasury, deposit, financial report