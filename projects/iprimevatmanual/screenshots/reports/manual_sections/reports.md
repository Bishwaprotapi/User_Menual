### Page: Audit Report

![Audit Report: Screen](screenshots/reports/audit_report.png)

**Page purpose:** This page provides a centralized hub to access various import, purchase, sales, and export audit data records.

**Route:** `/reports/otherReports/auditReport`

<!-- manual-meta: {"module": "Reports", "page": "Audit Report", "task": "View audit report categories", "action": "view", "roles": [], "route": "/reports/otherReports/auditReport", "screenshots": ["screenshots/reports/audit_report.png"], "keywords": ["audit", "import", "purchase", "sales", "export"], "task_order": 1} -->
#### Task: View audit report categories

**Purpose:** To navigate to specific audit report areas including Imports, Local Purchases, Local Sales, and Exports.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module

**Steps:**
1. Navigate to the Reports module in the sidebar.
2. Select 'Audit Report' from the MIS Report list.
3. Click on the desired category button (Import, Local Purchase, Local Sales, or Export) to view associated reports.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The user is directed to the relevant audit report dashboard based on the selected category.

**Warnings:**
* No specific warning was identified

**Search keywords:** audit, import, purchase, sales, export

### Page: Chok Ka/Kha Report

![Chok Ka Kha: Screen](screenshots/reports/chok_ka_kha.png)

![Chok Ka Kha: Show](screenshots/reports/chok_ka_kha_show.png)

**Page purpose:** This report displays financial data for Chok Ka and Chok Kha forms for a specified branch and date range.

**Route:** `/reports/otherReports/chok-ka/kha`

<!-- manual-meta: {"module": "Reports", "page": "Chok Ka/Kha Report", "task": "Filter Chok Ka/Kha records", "action": "filter", "roles": [], "route": "/reports/otherReports/chok-ka/kha", "screenshots": ["screenshots/reports/chok_ka_kha.png", "screenshots/reports/chok_ka_kha_show.png"], "keywords": ["chok ka", "chok kha", "financial report", "vat form"], "task_order": 1} -->
#### Task: Filter Chok Ka/Kha records

**Purpose:** To retrieve specific financial records for a given branch and time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the MIS Reports section.

**Steps:**
1. Navigate to 'Chok Ka/Kha' under the MIS Report section.
2. Select the desired branch from the 'Branch' dropdown.
3. Enter or select the 'From Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Branch:** Dropdown to select the organization branch.
* **From Date:** Date picker for the start of the report period.
* **To Date:** Date picker for the end of the report period.

**Expected result:** The report displays data if found, or displays a 'No Data Found' warning if the selection criteria yield no results.

**Warnings:**
* No specific warning was identified

**Search keywords:** chok ka, chok kha, financial report, vat form

### Page: Credit Note Report

![Credit Note Report: Screen](screenshots/reports/credit_note_report.png)

![Credit Note Report: Show](screenshots/reports/credit_note_report_show.png)

**Page purpose:** This page allows users to view a list of credit notes issued to partners within a specific branch and time frame.

**Route:** `/reports/otherReports/creditNoteReport`

<!-- manual-meta: {"module": "Reports", "page": "Credit Note Report", "task": "Search credit note records", "action": "search", "roles": [], "route": "/reports/otherReports/creditNoteReport", "screenshots": ["screenshots/reports/credit_note_report.png", "screenshots/reports/credit_note_report_show.png"], "keywords": ["credit note", "invoice", "vat correction"], "task_order": 1} -->
#### Task: Search credit note records

**Purpose:** To view credit notes for specific branches and date ranges.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Authorized access to reports.

**Steps:**
1. Select 'Credit Note Report' from the sidebar.
2. Select the 'Branch Name'.
3. Define the 'From Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Branch Name:** The branch context for the credit notes.
* **From Date:** Start date for transaction filtering.
* **To Date:** End date for transaction filtering.

**Expected result:** A table populated with credit note details such as Partner, Invoice, Fiscal Year, and Transaction Date appears below the search form.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, invoice, vat correction

### Page: Debit Note Report

![Debit Note Report: Screen](screenshots/reports/debit_note_report.png)

![Debit Note Report: Show](screenshots/reports/debit_note_report_show.png)

**Page purpose:** This page provides a filtered view of debit notes issued, enabling users to verify transaction history.

**Route:** `/reports/otherReports/debitNoteReport`

<!-- manual-meta: {"module": "Reports", "page": "Debit Note Report", "task": "View debit note report", "action": "view", "roles": [], "route": "/reports/otherReports/debitNoteReport", "screenshots": ["screenshots/reports/debit_note_report.png", "screenshots/reports/debit_note_report_show.png"], "keywords": ["debit note", "transaction history"], "task_order": 1} -->
#### Task: View debit note report

**Purpose:** To extract and verify debit note information for accounting purposes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have navigate access to the MIS reports.

**Steps:**
1. Select 'Debit Note Report' from the navigation menu.
2. Choose a 'Branch Name'.
3. Specify the date range using 'From Date' and 'To Date'.
4. Click 'View' to trigger the data pull.

**Fields and controls:**
* **Branch Name:** Identifier for the business entity branch.
* **From Date:** The date from which to start the report.
* **To Date:** The date at which the report ends.

**Expected result:** A populated report table including SL, Branch Name, Partner, Invoice, Fiscal Year, and Transaction Date.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, transaction history

### Page: Doc Verification System (DVS)

![Doc Verification System Dvs: Screen](screenshots/reports/doc_verification_system_dvs.png)

**Page purpose:** This page allows users to access the Document Verification System for validating financial and tax-related documents.

**Route:** `/reports/otherReports/docVerificationSystem(DVS)`

<!-- manual-meta: {"module": "Reports", "page": "Doc Verification System (DVS)", "task": "Access DVS portal", "action": "view", "roles": [], "route": "/reports/otherReports/docVerificationSystem(DVS)", "screenshots": ["screenshots/reports/doc_verification_system_dvs.png"], "keywords": ["dvs", "verification", "document check"], "task_order": 1} -->
#### Task: Access DVS portal

**Purpose:** To verify system documentation as required by VAT regulations.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Active session with DVS permissions.

**Steps:**
1. Navigate to the Reports module.
2. Select 'Doc Verification System (DVS)' from the list.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The screen loads the Doc Verification System interface.

**Warnings:**
* No specific warning was identified

**Search keywords:** dvs, verification, document check

### Page: HSCode Wise Sales & VAT

![Hscode Wise Sales Vat: Screen](screenshots/reports/hscode_wise_sales_vat.png)

![Hscode Wise Sales Vat: Show](screenshots/reports/hscode_wise_sales_vat_show.png)

**Page purpose:** This report provides a breakdown of sales quantity and VAT information categorized by HS Code and item.

**Route:** `/reports/otherReports/hsCodeVatSummary`

<!-- manual-meta: {"module": "Reports", "page": "HSCode Wise Sales & VAT", "task": "Filter HSCode VAT sales summary", "action": "filter", "roles": [], "route": "/reports/otherReports/hsCodeVatSummary", "screenshots": ["screenshots/reports/hscode_wise_sales_vat.png", "screenshots/reports/hscode_wise_sales_vat_show.png"], "keywords": ["hs code", "vat", "sales summary", "item code"], "task_order": 1} -->
#### Task: Filter HSCode VAT sales summary

**Purpose:** To analyze sales performance and VAT liability per HS Code.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be on the 'HSCode Wise Sales & Vat' page.

**Steps:**
1. Set the 'From Date' and 'To Date' range.
2. Click the 'View' button.

**Fields and controls:**
* **From Date:** Start of the sales data period.
* **To Date:** End of the sales data period.

**Expected result:** The report displays data including HS Code, Item Code, Item Name, Sales Quantity, Rate, Value, and VAT figures.

**Warnings:**
* No specific warning was identified

**Search keywords:** hs code, vat, sales summary, item code

### Page: Inventory Reconciliation

![Inventory Reconciliation: Screen](screenshots/reports/inventory_reconciliation.png)

**Page purpose:** A reporting page designed to reconcile inventory counts against records to ensure accuracy.

**Route:** `/reports/otherReports/inventoryReport`

<!-- manual-meta: {"module": "Reports", "page": "Inventory Reconciliation", "task": "Filter inventory data", "action": "filter", "roles": [], "route": "/reports/otherReports/inventoryReport", "screenshots": ["screenshots/reports/inventory_reconciliation.png"], "keywords": ["inventory", "reconciliation", "stock count"], "task_order": 1} -->
#### Task: Filter inventory data

**Purpose:** To generate an inventory reconciliation report for a specific time frame.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the Inventory Reconciliation menu.

**Steps:**
1. Select the 'View Type' from the dropdown.
2. Input the 'From Date' and 'To Date'.
3. Click the 'View' button to execute the search.

**Fields and controls:**
* **View Type:** Selector for the type of inventory view required.
* **From Date:** Beginning of the reconciliation period.
* **To Date:** Ending of the reconciliation period.

**Expected result:** Reconciliation data will be generated based on the chosen filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** inventory, reconciliation, stock count

### Page: Material Issue Report

![Material Issue Report: Screen](screenshots/reports/material_issue_report.png)

**Page purpose:** This page is used to report on material issuance for production or internal consumption.

**Route:** `/reports/otherReports/materialIssueReport`

<!-- manual-meta: {"module": "Reports", "page": "Material Issue Report", "task": "Generate material issue report", "action": "view", "roles": [], "route": "/reports/otherReports/materialIssueReport", "screenshots": ["screenshots/reports/material_issue_report.png"], "keywords": ["material issue", "stock consumption", "production supply"], "task_order": 1} -->
#### Task: Generate material issue report

**Purpose:** To view records of material consumption or transfers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to MIS reports.

**Steps:**
1. Select the 'Branch' from the dropdown.
2. Select a 'Sort By' option if required.
3. Enter the 'From Date' and 'To Date'.
4. Click 'View' to load the report.

**Fields and controls:**
* **Branch:** Select the relevant branch.
* **Sort By:** Defines the sort order of the output.
* **From Date:** Start date for material issues.
* **To Date:** End date for material issues.

**Expected result:** The report displays material issue data according to the selected branch and date range.

**Warnings:**
* No specific warning was identified

**Search keywords:** material issue, stock consumption, production supply

### Page: Mushak 9.1 (VAT Return)

![Mis Report: Screen](screenshots/reports/mis_report.png)

![Mis Report: Show](screenshots/reports/mis_report_show.png)

**Page purpose:** This page provides the official Value Added Tax (VAT) return form for submission.

**Route:** `/reports/mushakForms/mushak9.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 9.1 (VAT Return)", "task": "View VAT Return", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak9.1", "screenshots": ["screenshots/reports/mis_report.png", "screenshots/reports/mis_report_show.png"], "keywords": ["VAT", "Return", "Mushak 9.1"], "task_order": 1} -->
#### Task: View VAT Return

**Purpose:** To review the VAT return details for a specific month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* A valid month and year selected.

**Steps:**
1. Select the month and year from the month field.
2. Click the View button.

**Fields and controls:**
* **mushakDate:** The target month and year for the return.

**Expected result:** The VAT return form is populated with the corresponding data.

**Warnings:**
* No specific warning was identified

**Search keywords:** VAT, Return, Mushak 9.1

### Page: Mushak 4.3 (Price Declaration)

![Mushak 4 3 Price Declaration: Screen](screenshots/reports/mushak_4_3_price_declaration.png)

**Page purpose:** This page allows users to view the price declaration details of items.

**Route:** `/reports/mushakForms/mushak4.3`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.3 (Price Declaration)", "task": "Search Items", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak4.3", "screenshots": ["screenshots/reports/mushak_4_3_price_declaration.png"], "keywords": ["Price", "Declaration", "Mushak 4.3"], "task_order": 1} -->
#### Task: Search Items

**Purpose:** To quickly locate a specific item's price declaration.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the reports module.

**Steps:**
1. Enter the item name into the search field.
2. View the filtered result in the table.

**Fields and controls:**
* **Item Name Search:** Field to search for a specific item by name.

**Expected result:** The table updates to show items matching the search criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** Price, Declaration, Mushak 4.3

### Page: Mushak 4.4 (Item Destroy)

![Mushak 4 4 Item Destroy: Screen](screenshots/reports/mushak_4_4_item_destroy.png)

**Page purpose:** This page is used to view details of destroyed items.

**Route:** `/reports/mushakForms/mushak4.4`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.4 (Item Destroy)", "task": "Filter Item Destruction", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak4.4", "screenshots": ["screenshots/reports/mushak_4_4_item_destroy.png"], "keywords": ["Destroy", "Mushak 4.4"], "task_order": 1} -->
#### Task: Filter Item Destruction

**Purpose:** To view item destruction records within a specific timeframe.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Records exist for the selected period.

**Steps:**
1. Select the Branch, Item Type, and Item Name.
2. Select the From Date and To Date.
3. Click the View button.

**Fields and controls:**
* **Branch:** Select the branch for which data is required.
* **fromDate:** Start date for the report period.
* **toDate:** End date for the report period.

**Expected result:** Records matching the criteria are displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** Destroy, Mushak 4.4

### Page: Mushak 4.5 (Accident Destroy)

![Mushak 4 5 Accident Destroy: Screen](screenshots/reports/mushak_4_5_accident_destroy.png)

**Page purpose:** This page is used to view items destroyed due to accidents.

**Route:** `/reports/mushakForms/mushak4.5`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.5 (Accident Destroy)", "task": "Filter Accident Destruction", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak4.5", "screenshots": ["screenshots/reports/mushak_4_5_accident_destroy.png"], "keywords": ["Accident", "Destroy", "Mushak 4.5"], "task_order": 1} -->
#### Task: Filter Accident Destruction

**Purpose:** To view records of items lost due to accidents.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Relevant accident destruction logs exist.

**Steps:**
1. Select the Branch, Item Type, and Item Name.
2. Select the date range using From Date and To Date.
3. Click the View button.

**Fields and controls:**
* **fromDate:** The beginning date of the range.
* **toDate:** The end date of the range.

**Expected result:** The relevant accident destruction data is populated.

**Warnings:**
* No specific warning was identified

**Search keywords:** Accident, Destroy, Mushak 4.5

### Page: Mushak 4.6 (Waste Disposal)

![Mushak 4 6 Waste Disposal: Screen](screenshots/reports/mushak_4_6_waste_disposal.png)

**Page purpose:** This page provides an overview of waste disposal records.

**Route:** `/reports/mushakForms/mushak4.6`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.6 (Waste Disposal)", "task": "View Waste Disposal Logs", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak4.6", "screenshots": ["screenshots/reports/mushak_4_6_waste_disposal.png"], "keywords": ["Waste", "Disposal", "Mushak 4.6"], "task_order": 1} -->
#### Task: View Waste Disposal Logs

**Purpose:** To review historical waste disposal data.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Waste records have been previously logged.

**Steps:**
1. Navigate to the report page.
2. Review the generated table list.

**Fields and controls:**
* **rows per page:** Configures how many records show per page.

**Expected result:** The table shows the list of waste disposal events.

**Warnings:**
* No specific warning was identified

**Search keywords:** Waste, Disposal, Mushak 4.6

### Page: Mushak 6.10 (P&S +2 Lakh)

![Mushak 6 10 P S 2 Lakh: Screen](screenshots/reports/mushak_6_10_p_s_2_lakh.png)

![Mushak 6 10 P S 2 Lakh: Show](screenshots/reports/mushak_6_10_p_s_2_lakh_show.png)

**Page purpose:** This report summarizes purchases and sales over two lakh.

**Route:** `/reports/mushakForms/mushak6.10`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.10 (P&S +2 Lakh)", "task": "Generate P&S Report", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.10", "screenshots": ["screenshots/reports/mushak_6_10_p_s_2_lakh.png", "screenshots/reports/mushak_6_10_p_s_2_lakh_show.png"], "keywords": ["P&S", "2 Lakh", "Mushak 6.10"], "task_order": 1} -->
#### Task: Generate P&S Report

**Purpose:** To generate a report for large purchase and sales transactions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* A valid date range is selected.

**Steps:**
1. Select the Branch.
2. Pick the From Date and To Date.
3. Click the View button.

**Fields and controls:**
* **Branch:** Select the branch.

**Expected result:** Report data is populated. If not available, an error or notification will appear.

**Warnings:**
* No specific warning was identified

**Search keywords:** P&S, 2 Lakh, Mushak 6.10

### Page: Mushak 6.1 (Purchase Register)

![Mushak 6 1 Purchase Register: Screen](screenshots/reports/mushak_6_1_purchase_register.png)

**Page purpose:** This page displays the purchase register reports.

**Route:** `/reports/mushakForms/mushak6.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.1 (Purchase Register)", "task": "Filter Purchase Register", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.1", "screenshots": ["screenshots/reports/mushak_6_1_purchase_register.png"], "keywords": ["Purchase", "Register", "Mushak 6.1"], "task_order": 1} -->
#### Task: Filter Purchase Register

**Purpose:** To narrow down the purchase register data by date and type.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Available purchase data.

**Steps:**
1. Select Item Type and Branch.
2. Select From Date and To Date.
3. Select the display format (Bangla or English).
4. Click the View button.

**Fields and controls:**
* **Bangla format:** Display the report in Bengali.
* **English format:** Display the report in English.

**Expected result:** The purchase register is filtered according to the selected format and date range.

**Warnings:**
* No specific warning was identified

**Search keywords:** Purchase, Register, Mushak 6.1

### Page: Mushak 6.2.1 (P&S Register)

![Mushak 6 2 1 P S Register: Screen](screenshots/reports/mushak_6_2_1_p_s_register.png)

**Page purpose:** This page allows users to view the Purchases and Sales register.

**Route:** `/reports/mushakForms/mushak6-2-1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.2.1 (P&S Register)", "task": "Generate P&S Register", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6-2-1", "screenshots": ["screenshots/reports/mushak_6_2_1_p_s_register.png"], "keywords": ["P&S", "Register", "Mushak 6.2.1"], "task_order": 1} -->
#### Task: Generate P&S Register

**Purpose:** To generate a comprehensive report of purchases and sales.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* A date range has been specified.

**Steps:**
1. Select the Item Type, Branch, and Item Name.
2. Select the report date range.
3. Click the View button.

**Fields and controls:**
* **Item Type:** Type of item.

**Expected result:** The P&S register for the selected item and time period is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** P&S, Register, Mushak 6.2.1

### Page: Mushak 6.2 (Sales Register)

![Mushak 6 2 Sales Register: Screen](screenshots/reports/mushak_6_2_sales_register.png)

**Page purpose:** This page provides a report of sales records based on user-selected criteria.

**Route:** `/reports/mushakForms/mushak6.2`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.2 (Sales Register)", "task": "Filter and View Sales Register", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.2", "screenshots": ["screenshots/reports/mushak_6_2_sales_register.png"], "keywords": ["Sales report", "Sales Register", "Mushak 6.2"], "task_order": 1} -->
#### Task: Filter and View Sales Register

**Purpose:** To view a specific sales register report based on item type, branch, and date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must exist for the selected criteria.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.2 (Sales Register).
2. Select an Item Type from the dropdown.
3. Select a Branch.
4. Choose a From Date and To Date using the date picker.
5. Select a report format (Bangla or English).
6. Click the View button to display the report.

**Fields and controls:**
* **Item Type:** Dropdown to select the category of sales items.
* **Item:** Dropdown to specify the particular item name.
* **Branch:** Dropdown to select the relevant branch.
* **From Date:** The start date for the sales report.
* **To Date:** The end date for the sales report.

**Expected result:** A list of sales records corresponding to the selected filters, or a message stating 'Sales information not available'.

**Warnings:**
* If no records are found for the selected criteria, the system will display a notification message.

**Search keywords:** Sales report, Sales Register, Mushak 6.2

### Page: Mushak 6.3 (Sales Invoice)

![Mushak 6 3 Sales Invoice: Screen](screenshots/reports/mushak_6_3_sales_invoice.png)

![Mushak 6 3 Sales Invoice: Show](screenshots/reports/mushak_6_3_sales_invoice_show.png)

**Page purpose:** This page allows users to search and view sales invoice records.

**Route:** `/reports/mushakForms/mushak6.3`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.3 (Sales Invoice)", "task": "Search Sales Invoices", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.3", "screenshots": ["screenshots/reports/mushak_6_3_sales_invoice.png", "screenshots/reports/mushak_6_3_sales_invoice_show.png"], "keywords": ["Sales Invoice", "Invoice report", "Mushak 6.3"], "task_order": 1} -->
#### Task: Search Sales Invoices

**Purpose:** To find specific sales invoices for reporting or verification.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Invoices must be generated in the system.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.3 (Sales Invoice).
2. Select the Branch from the dropdown.
3. Set the From Date and To Date range.
4. Click the View button to generate the list.
5. Use the 'BOE, BIN, Inv No Search' field to narrow results if necessary.

**Fields and controls:**
* **Select Branch:** Dropdown to select the business branch.
* **BOE, BIN, Inv No Search:** Search input for filtering invoices by bill of entry, business identification number, or invoice number.

**Expected result:** A table populated with relevant sales invoices.

**Warnings:**
* No specific warning was identified

**Search keywords:** Sales Invoice, Invoice report, Mushak 6.3

### Page: Mushak 6.4 (Issue MFG.)

![Mushak 6 4 Issue Mfg: Screen](screenshots/reports/mushak_6_4_issue_mfg.png)

![Mushak 6 4 Issue Mfg: Show](screenshots/reports/mushak_6_4_issue_mfg_show.png)

**Page purpose:** Provides reports for contract manufacturing issue and receive transactions.

**Route:** `/reports/mushakForms/mushak6.4`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.4 (Issue MFG.)", "task": "View Contract Manufacturing Reports", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.4", "screenshots": ["screenshots/reports/mushak_6_4_issue_mfg.png", "screenshots/reports/mushak_6_4_issue_mfg_show.png"], "keywords": ["Manufacturing report", "Issue MFG", "Contract manufacturing"], "task_order": 1} -->
#### Task: View Contract Manufacturing Reports

**Purpose:** To report on raw materials issued or received for contract manufacturing.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Contract manufacturing transactions must have occurred.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.4 (Issue MFG.).
2. Toggle between the 'CONTRACT MANUFACTURING ISSUE' or 'CONTRACT MANUFACTURING RECEIVE' tabs.
3. Select the Branch, From Date, To Date, and Issue Type.
4. Click the View button.

**Fields and controls:**
* **Branch:** Select the relevant branch.
* **Issue Type:** Dropdown to define the type of issuance or receipt.

**Expected result:** A table showing transaction details like Challan No, Supplier, Date, and Quantity.

**Warnings:**
* No specific warning was identified

**Search keywords:** Manufacturing report, Issue MFG, Contract manufacturing

### Page: Mushak 6.5 (Stock Transfer)

![Mushak 6 5 Stock Transfer: Screen](screenshots/reports/mushak_6_5_stock_transfer.png)

![Mushak 6 5 Stock Transfer: Show](screenshots/reports/mushak_6_5_stock_transfer_show.png)

**Page purpose:** Used to monitor records of stock transfers between branches or locations.

**Route:** `/reports/mushakForms/mushak6.5`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.5 (Stock Transfer)", "task": "Browse Stock Transfers", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.5", "screenshots": ["screenshots/reports/mushak_6_5_stock_transfer.png", "screenshots/reports/mushak_6_5_stock_transfer_show.png"], "keywords": ["Stock transfer report", "Inventory movement"], "task_order": 1} -->
#### Task: Browse Stock Transfers

**Purpose:** To verify the history of stock movements.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Stock transfer transactions must be recorded.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.5 (Stock Transfer).
2. Select the Branch Name and Item Type.
3. Click the View button to load the transfer records.
4. Use the 'Transfer No Search' field to filter the table list.

**Fields and controls:**
* **Transfer No Search:** Filter table by transfer identification number.

**Expected result:** A list of stock transfers with details such as Transfer No, Branch, and Quantity.

**Warnings:**
* No specific warning was identified

**Search keywords:** Stock transfer report, Inventory movement

### Page: Mushak 6.6 (VDS Certificate)

![Mushak 6 6 Vds Certificate: Screen](screenshots/reports/mushak_6_6_vds_certificate.png)

![Mushak 6 6 Vds Certificate: Show](screenshots/reports/mushak_6_6_vds_certificate_show.png)

**Page purpose:** Used for reviewing VAT Deducted at Source (VDS) certificates.

**Route:** `/reports/mushakForms/mushak6.6`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.6 (VDS Certificate)", "task": "Review VDS Certificates", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.6", "screenshots": ["screenshots/reports/mushak_6_6_vds_certificate.png", "screenshots/reports/mushak_6_6_vds_certificate_show.png"], "keywords": ["VDS", "VAT Deducted at Source", "Certificate report"], "task_order": 1} -->
#### Task: Review VDS Certificates

**Purpose:** To audit and view the status of VDS certificates.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* VDS entries must exist in the system.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.6 (VDS Certificate).
2. Select the Report Type (e.g., VDS Certificate Issue) and the Branch.
3. Enter the date range.
4. Select a status filter: All, Pending, or Complete.
5. Click the View button.

**Fields and controls:**
* **Select Report Type:** Dropdown to select certificate type.
* **Status Filter:** Radio buttons to filter by certificate completion status (All, Pending, Complete).

**Expected result:** Table showing certificates including Certificate No, Chalan No, and Deducted Amount.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, VAT Deducted at Source, Certificate report

### Page: Mushak 6.7 (Credit Note)

![Mushak 6 7 Credit Note: Screen](screenshots/reports/mushak_6_7_credit_note.png)

**Page purpose:** Provides a report of issued credit notes.

**Route:** `/reports/mushakForms/mushak6.7`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.7 (Credit Note)", "task": "Search Credit Notes", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.7", "screenshots": ["screenshots/reports/mushak_6_7_credit_note.png"], "keywords": ["Credit Note", "Return report"], "task_order": 1} -->
#### Task: Search Credit Notes

**Purpose:** To find and review specific credit notes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Credit notes must have been created.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.7 (Credit Note).
2. Select Branch and Date range.
3. Use the 'Sales Invoice Search' box to find related notes.
4. Click View.

**Fields and controls:**
* **Sales Invoice Search:** Search input for credit notes related to specific sales invoices.

**Expected result:** A table populated with credit note details.

**Warnings:**
* No specific warning was identified

**Search keywords:** Credit Note, Return report

### Page: Mushak 6.8 (Debit Note)

![Mushak 6 8 Debit Note: Screen](screenshots/reports/mushak_6_8_debit_note.png)

![Mushak 6 8 Debit Note: Show](screenshots/reports/mushak_6_8_debit_note_show.png)

**Page purpose:** Provides a report of issued debit notes.

**Route:** `/reports/mushakForms/mushak6.8`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.8 (Debit Note)", "task": "Search Debit Notes", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.8", "screenshots": ["screenshots/reports/mushak_6_8_debit_note.png", "screenshots/reports/mushak_6_8_debit_note_show.png"], "keywords": ["Debit Note"], "task_order": 1} -->
#### Task: Search Debit Notes

**Purpose:** To find and review specific debit notes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Debit notes must have been created.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.8 (Debit Note).
2. Select the Branch Name, Form Date, and To Date.
3. Use the 'Purchase Invoice Search' to find related notes.
4. Click View.

**Fields and controls:**
* **Purchase Invoice Search:** Search input for debit notes related to specific purchase invoices.

**Expected result:** A table populated with debit note details.

**Warnings:**
* No specific warning was identified

**Search keywords:** Debit Note

### Page: Mushak 9.1 (VAT Return)

![Mushak 9 1 Vat Return: Screen](screenshots/reports/mushak_9_1_vat_return.png)

![Mushak 9 1 Vat Return: Show](screenshots/reports/mushak_9_1_vat_return_show.png)

**Page purpose:** Used to generate, view, and print the official VAT Return form.

**Route:** `/reports/mushakForms/mushak9.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 9.1 (VAT Return)", "task": "Generate VAT Return", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak9.1", "screenshots": ["screenshots/reports/mushak_9_1_vat_return.png", "screenshots/reports/mushak_9_1_vat_return_show.png"], "keywords": ["VAT Return", "Mushak 9.1", "Tax return"], "task_order": 1} -->
#### Task: Generate VAT Return

**Purpose:** To view the VAT return details for a selected month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Transactions for the period must be recorded and posted.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 9.1 (VAT Return).
2. Select the Month/Year in the 'Year And Month' field.
3. Click the View button to display the form.
4. Click the Print button to output the form, or Posting to commit the return.

**Fields and controls:**
* **Year And Month:** Select the period for the VAT return.

**Expected result:** The VAT return form is populated with the financial summary for the selected period.

**Warnings:**
* No specific warning was identified

**Search keywords:** VAT Return, Mushak 9.1, Tax return

### Page: Mushak Forms

![Mushak Forms: Screen](screenshots/reports/mushak_forms.png)

![Mushak Forms: Show](screenshots/reports/mushak_forms_show.png)

**Page purpose:** This page provides access to various government-mandated VAT forms and registers for record-keeping and compliance reporting.

**Route:** `/reports/mushakForms`

<!-- manual-meta: {"module": "Reports", "page": "Mushak Forms", "task": "View Mushak Report", "action": "view", "roles": [], "route": "/reports/mushakForms", "screenshots": ["screenshots/reports/mushak_forms.png", "screenshots/reports/mushak_forms_show.png"], "keywords": ["Mushak", "VAT form", "register", "compliance report"], "task_order": 1} -->
#### Task: View Mushak Report

**Purpose:** To generate and view specific VAT-related reports like purchase or sales registers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have navigation access to Reports

**Steps:**
1. Navigate to the Reports module
2. Click on 'Mushak Forms' to expand the list
3. Select the desired Mushak form (e.g., Mushak 6.2 Sales Register)
4. Select the branch and date range as required
5. Click the 'View' button

**Fields and controls:**
* **Select Branch:** Dropdown to select the company branch.
* **Enter From Date:** Date picker for the start of the report range.
* **Enter To Date:** Date picker for the end of the report range.

**Expected result:** A table populated with relevant record data based on the chosen filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** Mushak, VAT form, register, compliance report

### Page: Partner Vs Stock Report

![Partner Vs Stock: Screen](screenshots/reports/partner_vs_stock.png)

**Page purpose:** This report displays a comparison of stock levels relative to partners/customers.

**Route:** `/reports/otherReports/partnerVsStock`

<!-- manual-meta: {"module": "Reports", "page": "Partner Vs Stock Report", "task": "View Partner Vs Stock Report", "action": "view", "roles": [], "route": "/reports/otherReports/partnerVsStock", "screenshots": ["screenshots/reports/partner_vs_stock.png"], "keywords": ["stock report", "partner inventory", "stock analysis"], "task_order": 1} -->
#### Task: View Partner Vs Stock Report

**Purpose:** To analyze stock inventory details associated with specific partners.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Active session in Prime VAT

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Partner Vs Stock' from the left sidebar
3. Choose a branch, customer name, and item filter
4. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the company branch.
* **Customer Name:** Field to filter by a specific customer.
* **Item:** Dropdown to select a specific stock item.

**Expected result:** The grid populates with item names, codes, units of measurement, price, and current stock status.

**Warnings:**
* No specific warning was identified

**Search keywords:** stock report, partner inventory, stock analysis

### Page: Payment Method Wise Report

![Payment Method Wise Report: Screen](screenshots/reports/payment_method_wise_report.png)

![Payment Method Wise Report: Show](screenshots/reports/payment_method_wise_report_show.png)

**Page purpose:** Displays financial reports categorized by the payment methods used for transactions.

**Route:** `/reports/otherReports/paymentMethodWiseReport`

<!-- manual-meta: {"module": "Reports", "page": "Payment Method Wise Report", "task": "View Payment Method Wise Report", "action": "view", "roles": [], "route": "/reports/otherReports/paymentMethodWiseReport", "screenshots": ["screenshots/reports/payment_method_wise_report.png", "screenshots/reports/payment_method_wise_report_show.png"], "keywords": ["payment summary", "transaction audit", "financial report"], "task_order": 1} -->
#### Task: View Payment Method Wise Report

**Purpose:** To audit and view transaction summaries based on the payment method (e.g., cash, credit, bank transfer).

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to MIS reports

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Payment Method Wise Report'
3. Specify Item Type, Payment Method Type, and date range
4. Click the 'View' button

**Fields and controls:**
* **Item Type:** Category of items for the report (e.g., Sales).
* **Payment Method Type:** Filter by payment method or 'All'.

**Expected result:** A data view displaying transactions grouped by payment method.

**Warnings:**
* No specific warning was identified

**Search keywords:** payment summary, transaction audit, financial report

### Page: Production Report

![Production Report: Screen](screenshots/reports/production_report.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/reports/otherReports/productionReport`

<!-- manual-meta: {"module": "Reports", "page": "Production Report", "task": "Use Production Report", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/reports/otherReports/productionReport", "screenshots": ["screenshots/reports/production_report.png"], "keywords": ["Production Report", "production report"], "task_order": 1} -->
#### Task: Use Production Report

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Production Report page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Production Report, production report

### Page: Purchase Report

![Purchase Report: Screen](screenshots/reports/purchase_report.png)

![Purchase Report: Show](screenshots/reports/purchase_report_show.png)

**Page purpose:** Generates a detailed report of all procurement and purchase transactions.

**Route:** `/reports/otherReports/purchaseReport`

<!-- manual-meta: {"module": "Reports", "page": "Purchase Report", "task": "View Purchase Report", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseReport", "screenshots": ["screenshots/reports/purchase_report.png", "screenshots/reports/purchase_report_show.png"], "keywords": ["procurement", "purchase audit", "vendor report"], "task_order": 1} -->
#### Task: View Purchase Report

**Purpose:** To review purchase transaction logs over a specified time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Procurement data must exist in the system

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Purchase Report'
3. Set the Branch, Sort By, and date range filters
4. Click 'View'

**Fields and controls:**
* **Branch:** Filter for the organizational branch.
* **Sort By:** Defines the sort order of the resulting report.

**Expected result:** A list of purchase transactions matching the applied filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** procurement, purchase audit, vendor report

### Page: Purchase Report by Category

![Purchase Report By Category: Screen](screenshots/reports/purchase_report_by_category.png)

![Purchase Report By Category: Show](screenshots/reports/purchase_report_by_category_show.png)

**Page purpose:** Provides purchase transaction information organized by item categories.

**Route:** `/reports/otherReports/purchaseReportByCategory`

<!-- manual-meta: {"module": "Reports", "page": "Purchase Report by Category", "task": "View Category-wise Purchase Report", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseReportByCategory", "screenshots": ["screenshots/reports/purchase_report_by_category.png", "screenshots/reports/purchase_report_by_category_show.png"], "keywords": ["categorized purchase", "item classification", "procurement summary"], "task_order": 1} -->
#### Task: View Category-wise Purchase Report

**Purpose:** To analyze purchase volumes categorized by item groupings.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Items must be assigned to categories

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Purchase Report by Category'
3. Select the desired date range
4. Click 'View'

**Fields and controls:**
* **Enter From Date:** Start date for report extraction.
* **Enter To Date:** End date for report extraction.

**Expected result:** Categorized purchase transaction summaries appear on the screen.

**Warnings:**
* No specific warning was identified

**Search keywords:** categorized purchase, item classification, procurement summary

### Page: Purchase/Sales Details

![Purchase Sales Details: Screen](screenshots/reports/purchase_sales_details.png)

**Page purpose:** Offers a comprehensive view of both purchase and sales transaction details.

**Route:** `/reports/otherReports/purchaseSalesDetails`

<!-- manual-meta: {"module": "Reports", "page": "Purchase/Sales Details", "task": "View Purchase and Sales Details", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseSalesDetails", "screenshots": ["screenshots/reports/purchase_sales_details.png"], "keywords": ["transaction log", "audit", "detailed report"], "task_order": 1} -->
#### Task: View Purchase and Sales Details

**Purpose:** To view granular data for both sales and purchase operations in one report.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* System must contain both sales and purchase data

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Purchase/Sales Details'
3. Choose date range and record type (Purchase or Sales)
4. Click 'View'

**Fields and controls:**
* **Select Type:** Toggle between Purchase or Sales view.

**Expected result:** A detailed table of transactions based on the selected type.

**Warnings:**
* No specific warning was identified

**Search keywords:** transaction log, audit, detailed report

### Page: Wastage Sales

![Reports: Screen](screenshots/reports/reports.png)

![Reports: Show](screenshots/reports/reports_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/reports`

<!-- manual-meta: {"module": "Reports", "page": "Wastage Sales", "task": "Use Wastage Sales", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/reports", "screenshots": ["screenshots/reports/reports.png", "screenshots/reports/reports_show.png"], "keywords": ["Wastage Sales", "reports"], "task_order": 1} -->
#### Task: Use Wastage Sales

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Wastage Sales page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.
* **BOE, BIN, Inv No Search:** Visible text control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Wastage Sales, reports

### Page: Sales & Purchase Compare

![Sales Purchase Compare: Screen](screenshots/reports/sales_purchase_compare.png)

![Sales Purchase Compare: Show](screenshots/reports/sales_purchase_compare_show.png)

**Page purpose:** This page provides a comparison between sales and purchase data to analyze trends or discrepancies over specific dates.

**Route:** `/reports/otherReports/salesAndPurchaseCompare`

<!-- manual-meta: {"module": "Reports", "page": "Sales & Purchase Compare", "task": "View Sales & Purchase Comparison", "action": "view", "roles": [], "route": "/reports/otherReports/salesAndPurchaseCompare", "screenshots": ["screenshots/reports/sales_purchase_compare.png", "screenshots/reports/sales_purchase_compare_show.png"], "keywords": ["comparison", "sales vs purchase", "report", "analysis"], "task_order": 1} -->
#### Task: View Sales & Purchase Comparison

**Purpose:** To compare the sales and purchase data between two selected dates.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must be available for the selected dates.

**Steps:**
1. Navigate to Reports > MIS Report > Sales & Purchase Compare.
2. Select the Branch from the dropdown.
3. Select the Type.
4. Select the Based On frequency (e.g., Day).
5. Select the Purchase Compare (Date).
6. Select the Sales Compare (Date).
7. Click the View button.

**Fields and controls:**
* **Branch:** Dropdown to select the relevant branch.
* **Type:** Dropdown for report type selection.
* **Based On:** Dropdown for time frequency selection.
* **Purchase Compare (Date):** Date picker for the purchase data start point.
* **Sales Compare (Date):** Date picker for the sales data comparison point.

**Expected result:** The system displays a table comparing Amount, VAT, and Grand Total for both Purchase and Sales criteria.

**Warnings:**
* If no data exists for the selected dates, a 'No data found' message will appear.

**Search keywords:** comparison, sales vs purchase, report, analysis

### Page: Sales Report

![Sales Report: Screen](screenshots/reports/sales_report.png)

**Page purpose:** This page provides a detailed report of sales transactions within a specific date range.

**Route:** `/reports/otherReports/salesReport`

<!-- manual-meta: {"module": "Reports", "page": "Sales Report", "task": "Generate Sales Report", "action": "view", "roles": [], "route": "/reports/otherReports/salesReport", "screenshots": ["screenshots/reports/sales_report.png"], "keywords": ["sales", "invoices", "transactions", "report"], "task_order": 1} -->
#### Task: Generate Sales Report

**Purpose:** To view a summary or detailed list of sales transactions for a chosen period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Report.
2. Select the Branch.
3. Select the sorting preference in 'Sort By'.
4. Pick the 'From Date'.
5. Pick the 'To Date'.
6. Click the View button.

**Fields and controls:**
* **Branch:** Dropdown to select the branch.
* **Sort By:** Criteria to sort the report data.
* **From Date:** Starting date for the report range.
* **To Date:** Ending date for the report range.

**Expected result:** A list of sales transactions matching the specified criteria is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoices, transactions, report

### Page: Sales Report by Category

![Sales Report By Category: Screen](screenshots/reports/sales_report_by_category.png)

![Sales Report By Category: Show](screenshots/reports/sales_report_by_category_show.png)

**Page purpose:** This page displays sales data filtered by product categories for a specific date range.

**Route:** `/reports/otherReports/salesReportByCategory`

<!-- manual-meta: {"module": "Reports", "page": "Sales Report by Category", "task": "View Category-Wise Sales", "action": "view", "roles": [], "route": "/reports/otherReports/salesReportByCategory", "screenshots": ["screenshots/reports/sales_report_by_category.png", "screenshots/reports/sales_report_by_category_show.png"], "keywords": ["sales report", "category", "product group"], "task_order": 1} -->
#### Task: View Category-Wise Sales

**Purpose:** To analyze sales performance categorized by product groups.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Report by Category.
2. Select the 'Enter From Date'.
3. Select the 'Enter To Date'.
4. Click the View button.

**Fields and controls:**
* **Enter From Date:** The start date for the sales category report.
* **Enter To Date:** The end date for the sales category report.

**Expected result:** Displays a breakdown of sales figures organized by category for the selected date range.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales report, category, product group

### Page: Sales & Stock Summary

![Sales Stock Summary: Screen](screenshots/reports/sales_stock_summary.png)

![Sales Stock Summary: Show](screenshots/reports/sales_stock_summary_show.png)

**Page purpose:** This page generates a combined summary report showing sales performance against current stock levels for a selected month.

**Route:** `/reports/otherReports/SalesStockSummary`

<!-- manual-meta: {"module": "Reports", "page": "Sales & Stock Summary", "task": "View Sales and Stock Summary", "action": "view", "roles": [], "route": "/reports/otherReports/SalesStockSummary", "screenshots": ["screenshots/reports/sales_stock_summary.png", "screenshots/reports/sales_stock_summary_show.png"], "keywords": ["stock summary", "inventory", "sales", "monthly report"], "task_order": 1} -->
#### Task: View Sales and Stock Summary

**Purpose:** To view the correlation between purchase, sales, and closing stock for a specific month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales & Stock Summary.
2. Select the Month and Year.
3. Click the View button.

**Fields and controls:**
* **Month:** The target month and year for the summary report.

**Expected result:** The system populates a report table with columns including Opening QTY, Purchase/Sales Info, and Closing Stock.

**Warnings:**
* No specific warning was identified

**Search keywords:** stock summary, inventory, sales, monthly report

### Page: Sales Summary Report

![Sales Summary Report: Screen](screenshots/reports/sales_summary_report.png)

![Sales Summary Report: Show](screenshots/reports/sales_summary_report_show.png)

**Page purpose:** A high-level overview of sales summaries based on branch and date range.

**Route:** `/reports/otherReports/salesSummaryReport`

<!-- manual-meta: {"module": "Reports", "page": "Sales Summary Report", "task": "Generate Sales Summary Report", "action": "view", "roles": [], "route": "/reports/otherReports/salesSummaryReport", "screenshots": ["screenshots/reports/sales_summary_report.png", "screenshots/reports/sales_summary_report_show.png"], "keywords": ["summary", "invoice list", "sales"], "task_order": 1} -->
#### Task: Generate Sales Summary Report

**Purpose:** To generate an invoice-level summary of sales transactions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Summary Report.
2. Select the branch from 'Select Branch'.
3. Select the 'Enter From Date'.
4. Select the 'Enter To Date'.
5. Click the View button.

**Fields and controls:**
* **Select Branch:** Dropdown to select the branch.
* **Enter From Date:** Start date for the summary range.
* **Enter To Date:** End date for the summary range.

**Expected result:** A table summarizing Sales Inv No, Trade Type, Customer Name, and other transaction details.

**Warnings:**
* No specific warning was identified

**Search keywords:** summary, invoice list, sales

### Page: Stock Reconcile Report

![Stock Reconsile Report: Screen](screenshots/reports/stock_reconsile_report.png)

**Page purpose:** This page is used for reconciling stock discrepancies.

**Route:** `/reports/otherReports/stockReconsileReport`

<!-- manual-meta: {"module": "Reports", "page": "Stock Reconcile Report", "task": "View Stock Reconcile Report", "action": "view", "roles": [], "route": "/reports/otherReports/stockReconsileReport", "screenshots": ["screenshots/reports/stock_reconsile_report.png"], "keywords": ["reconcile", "stock", "audit"], "task_order": 1} -->
#### Task: View Stock Reconcile Report

**Purpose:** To check for differences between recorded and actual stock levels.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Stock Reconsile Report.
2. Select the Branch.
3. Select the From Date.
4. Click the View button.

**Fields and controls:**
* **Branch:** Select the branch for reconciliation.
* **From Date:** Date to begin reconciliation check.

**Expected result:** System populates the reconciliation findings.

**Warnings:**
* No specific warning was identified

**Search keywords:** reconcile, stock, audit

### Page: Stock Register

![Stock Register: Screen](screenshots/reports/stock_register.png)

![Stock Register: Show](screenshots/reports/stock_register_show.png)

**Page purpose:** Provides a full record of all stock movements, including opening, receipt, and issue quantities.

**Route:** `/reports/otherReports/stockRegister`

<!-- manual-meta: {"module": "Reports", "page": "Stock Register", "task": "Generate Stock Register", "action": "view", "roles": [], "route": "/reports/otherReports/stockRegister", "screenshots": ["screenshots/reports/stock_register.png", "screenshots/reports/stock_register_show.png"], "keywords": ["register", "inventory", "stock level", "closing balance"], "task_order": 1} -->
#### Task: Generate Stock Register

**Purpose:** To view current and historical stock balances and closing values.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Stock Register.
2. Select the Branch.
3. Select the Item Type.
4. Enter From Date.
5. Enter To Date.
6. Click the View button.

**Fields and controls:**
* **Select Branch:** Dropdown for branch selection.
* **Item Type:** Select category of items.
* **Negative Stock:** Checkbox to filter for items with negative quantities.

**Expected result:** A detailed table showing opening, received, issued, and closing quantities/values for items.

**Warnings:**
* No specific warning was identified

**Search keywords:** register, inventory, stock level, closing balance

<!-- manual-meta: {"module": "Reports", "page": "Stock Register", "task": "Export Stock Register", "action": "export", "roles": [], "route": "/reports/otherReports/stockRegister", "screenshots": ["screenshots/reports/stock_register.png", "screenshots/reports/stock_register_show.png"], "keywords": ["download", "export", "spreadsheet"], "task_order": 2} -->
#### Task: Export Stock Register

**Purpose:** To export stock data to a spreadsheet format.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must be populated in the view.

**Steps:**
1. Perform the view generation steps.
2. Click the Excel Download button.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** A file is downloaded to the local device containing the current stock register report.

**Warnings:**
* No specific warning was identified

**Search keywords:** download, export, spreadsheet

### Page: Transaction Log

![Transaction Log: Screen](screenshots/reports/transaction_log.png)

**Page purpose:** Displays logs of system transactions for auditing purposes.

**Route:** `/reports/otherReports/auditLog`

<!-- manual-meta: {"module": "Reports", "page": "Transaction Log", "task": "View Transaction Logs", "action": "view", "roles": [], "route": "/reports/otherReports/auditLog", "screenshots": ["screenshots/reports/transaction_log.png"], "keywords": ["audit log", "history", "tracking"], "task_order": 1} -->
#### Task: View Transaction Logs

**Purpose:** To review historical transaction activity in the system.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Transaction Log.
2. Select the View Type.
3. Select From Date.
4. Select To Date.
5. Click the View button.

**Fields and controls:**
* **View Type:** Select the category of log to view.
* **From Date:** Starting date for the logs.
* **To Date:** Ending date for the logs.

**Expected result:** System displays a list of transactions matching the date and type criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** audit log, history, tracking

### Page: Transit Report

![Transit Report: Screen](screenshots/reports/transit_report.png)

![Transit Report: Show](screenshots/reports/transit_report_show.png)

**Page purpose:** This page provides a report on items currently in transit, including transfer details between branches.

**Route:** `/reports/otherReports/transitReport`

<!-- manual-meta: {"module": "Reports", "page": "Transit Report", "task": "View Transit Report", "action": "view", "roles": [], "route": "/reports/otherReports/transitReport", "screenshots": ["screenshots/reports/transit_report.png", "screenshots/reports/transit_report_show.png"], "keywords": ["transfer", "stock movement", "transit", "branch transfer"], "task_order": 1} -->
#### Task: View Transit Report

**Purpose:** To monitor and review stock movement between different branches.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module
* Data availability for the selected branch and date range

**Steps:**
1. Navigate to the Reports menu in the left sidebar.
2. Select 'Transit Report' from the MIS Report list.
3. Select the 'Branch' from the dropdown menu.
4. Select the 'Item Type' from the dropdown menu.
5. Enter the 'From Date' and 'To Date' in the respective date fields.
6. Click the 'View' button.

**Fields and controls:**
* **Branch:** Select the source or target branch for the report.
* **Item Type:** The category or type of items to be reported.
* **From Date:** The start date for the transit report period.
* **To Date:** The end date for the transit report period.

**Expected result:** The system displays a table containing transfer details such as Branch Name, Transfer Date, Transfer No, Qty information, and Narration, or an 'Data Not Found' message if no records exist.

**Warnings:**
* If no matching data is found for the selected criteria, a 'Data Not Found' message will appear.

**Search keywords:** transfer, stock movement, transit, branch transfer

### Page: Treasury Deposit Report

![Treasury Deposit Report: Screen](screenshots/reports/treasury_deposit_report.png)

![Treasury Deposit Report: Show](screenshots/reports/treasury_deposit_report_show.png)

**Page purpose:** This page provides a consolidated report of treasury deposits within a specified timeframe.

**Route:** `/reports/otherReports/treasuryDepositReport`

<!-- manual-meta: {"module": "Reports", "page": "Treasury Deposit Report", "task": "View Treasury Deposit Report", "action": "view", "roles": [], "route": "/reports/otherReports/treasuryDepositReport", "screenshots": ["screenshots/reports/treasury_deposit_report.png", "screenshots/reports/treasury_deposit_report_show.png"], "keywords": ["deposit", "treasury", "bank deposit"], "task_order": 1} -->
#### Task: View Treasury Deposit Report

**Purpose:** To view and verify records of deposits made to the treasury.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module
* Data availability within the selected date range

**Steps:**
1. Navigate to the Reports menu in the left sidebar.
2. Select 'Treasury Deposit Report' from the MIS Report list.
3. Enter the 'From Date'.
4. Enter the 'To Date'.
5. Click the 'View' button.

**Fields and controls:**
* **From Date:** The start date for the treasury deposit record search.
* **To Date:** The end date for the treasury deposit record search.

**Expected result:** The system displays the list of treasury deposits for the selected date range, or a 'Data Not Found' message if no records are available.

**Warnings:**
* A 'Data Not Found' message indicates no treasury records exist for the specified date range.

**Search keywords:** deposit, treasury, bank deposit