### Page: Contract Manufacturing Issue

![Contract Manufacturing Issue: Screen](screenshots/operation/contract_manufacturing_issue.png)

![Contract Manufacturing Issue: Show](screenshots/operation/contract_manufacturing_issue_show.png)

**Page purpose:** This page is used to view and manage raw materials issued for contract manufacturing processes.

**Route:** `/operation/manufacturing/contactManufacturing`

<!-- manual-meta: {"module": "Operation", "page": "Contract Manufacturing Issue", "task": "View Contract Manufacturing Issues", "action": "view", "roles": [], "route": "/operation/manufacturing/contactManufacturing", "screenshots": ["screenshots/operation/contract_manufacturing_issue.png", "screenshots/operation/contract_manufacturing_issue_show.png"], "keywords": ["manufacturing", "issue", "raw material", "contract"], "task_order": 1} -->
#### Task: View Contract Manufacturing Issues

**Purpose:** To list contract manufacturing issue records for a specific date range and branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Manufacturing module

**Steps:**
1. Navigate to Operation > Manufacturing > Contract Manufacturing Issue
2. Select the Branch from the dropdown
3. Select the 'From Date'
4. Select the 'To Date'
5. Select the Issue Type
6. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the relevant branch office.
* **From Date:** Starting date for the record search.
* **To Date:** Ending date for the record search.
* **Issue Type:** Type of manufacturing issue (e.g., Issue Raw Material).

**Expected result:** A table displaying records matching the specified filter criteria appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** manufacturing, issue, raw material, contract

### Page: Contract Manufacturing Receive

![Contract Manufacturing Receive: Screen](screenshots/operation/contract_manufacturing_receive.png)

![Contract Manufacturing Receive: Show](screenshots/operation/contract_manufacturing_receive_show.png)

**Page purpose:** This page is used to manage the receipt of raw materials back from contract manufacturing.

**Route:** `/operation/manufacturing/contactMFGReceive`

<!-- manual-meta: {"module": "Operation", "page": "Contract Manufacturing Receive", "task": "View Contract Manufacturing Receipts", "action": "view", "roles": [], "route": "/operation/manufacturing/contactMFGReceive", "screenshots": ["screenshots/operation/contract_manufacturing_receive.png", "screenshots/operation/contract_manufacturing_receive_show.png"], "keywords": ["receive", "raw material", "manufacturing", "receipt"], "task_order": 1} -->
#### Task: View Contract Manufacturing Receipts

**Purpose:** To view records of raw materials received from contract manufacturing.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Manufacturing module

**Steps:**
1. Navigate to Operation > Manufacturing > Contract Manufacturing Receive
2. Select the Branch
3. Define the date range using 'From Date' and 'To Date'
4. Select the Receive Type
5. Click the 'View' button

**Fields and controls:**
* **Branch:** The branch associated with the receipt.
* **From Date:** Beginning of the date range.
* **To Date:** End of the date range.
* **Receive Type:** The category of receipt (e.g., Receive Raw Material).

**Expected result:** A list of receipt transactions is displayed in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** receive, raw material, manufacturing, receipt

### Page: Credit Note

![Credit Note: Screen](screenshots/operation/credit_note.png)

**Page purpose:** This page allows users to view and search for sales credit notes.

**Route:** `/operation/sales/credit-note`

<!-- manual-meta: {"module": "Operation", "page": "Credit Note", "task": "Search Credit Notes", "action": "search", "roles": [], "route": "/operation/sales/credit-note", "screenshots": ["screenshots/operation/credit_note.png"], "keywords": ["credit note", "sales", "invoice"], "task_order": 1} -->
#### Task: Search Credit Notes

**Purpose:** To filter and locate specific credit notes issued to customers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Sales module

**Steps:**
1. Navigate to Operation > Sales > Credit Note
2. Select the Branch
3. Set the 'Form Date' and 'To Date'
4. Enter a value in the 'Sales Invoice Search' field
5. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the branch for the credit note.
* **Form Date:** Start date for the search.
* **To Date:** End date for the search.
* **Sales Invoice Search:** Keyword search for specific sales invoices.

**Expected result:** Credit note records matching the search criteria are displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, sales, invoice

### Page: Debit Note

![Debit Note: Screen](screenshots/operation/debit_note.png)

![Debit Note: Show](screenshots/operation/debit_note_show.png)

**Page purpose:** This page is used to view and search for purchase-related debit notes.

**Route:** `/operation/purchase/debit-note`

<!-- manual-meta: {"module": "Operation", "page": "Debit Note", "task": "View Debit Notes", "action": "view", "roles": [], "route": "/operation/purchase/debit-note", "screenshots": ["screenshots/operation/debit_note.png", "screenshots/operation/debit_note_show.png"], "keywords": ["debit note", "purchase", "invoice"], "task_order": 1} -->
#### Task: View Debit Notes

**Purpose:** To list debit notes associated with purchase invoices.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Purchase module

**Steps:**
1. Navigate to Operation > Purchase > Debit Note
2. Select the Branch Name
3. Specify the date range
4. Click the 'View' button

**Fields and controls:**
* **Branch Name:** Select the relevant branch.
* **Form Date:** Start date for reporting.
* **To Date:** End date for reporting.
* **Purchase Invoice Search:** Search for specific purchase invoices.

**Expected result:** The table populates with debit note details based on search filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, purchase, invoice

### Page: Vehicle

![Inventory Transaction: Screen](screenshots/operation/inventory_transaction.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/inventoryTransaction`

<!-- manual-meta: {"module": "Operation", "page": "Vehicle", "task": "Use Vehicle", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/inventoryTransaction", "screenshots": ["screenshots/operation/inventory_transaction.png"], "keywords": ["Vehicle", "inventory transaction"], "task_order": 1} -->
#### Task: Use Vehicle

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Vehicle page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Vehicle No & Code:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Vehicle, inventory transaction

### Page: Item Destroy

![Item Destroy: Screen](screenshots/operation/item_destroy.png)

![Item Destroy: Show](screenshots/operation/item_destroy_show.png)

**Page purpose:** This page is used to manage records of items that have been destroyed or written off.

**Route:** `/operation/inventoryTransaction/itemDestroy`

<!-- manual-meta: {"module": "Operation", "page": "Item Destroy", "task": "View Destroyed Items", "action": "view", "roles": [], "route": "/operation/inventoryTransaction/itemDestroy", "screenshots": ["screenshots/operation/item_destroy.png", "screenshots/operation/item_destroy_show.png"], "keywords": ["item destroy", "write off", "inventory"], "task_order": 1} -->
#### Task: View Destroyed Items

**Purpose:** To see a report of items destroyed within a specified date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Inventory Transaction module

**Steps:**
1. Navigate to Operation > Inventory Transaction > Item Destroy
2. Select the Branch Name
3. Set the 'From Date' and 'To Date'
4. Select the Item Type
5. Click the 'View' button

**Fields and controls:**
* **Branch Name:** Select the branch for inventory tracking.
* **From Date:** Start date for the list.
* **To Date:** End date for the list.
* **Item Type:** Category of the items (e.g., Purchase Book Item).

**Expected result:** Displays a filtered list of destroyed items.

**Warnings:**
* No specific warning was identified

**Search keywords:** item destroy, write off, inventory

### Page: Transfer Out

![Manufacturing: Screen](screenshots/operation/manufacturing.png)

![Manufacturing: Show](screenshots/operation/manufacturing_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/manufacturing`

<!-- manual-meta: {"module": "Operation", "page": "Transfer Out", "task": "Use Transfer Out", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/manufacturing", "screenshots": ["screenshots/operation/manufacturing.png", "screenshots/operation/manufacturing_show.png"], "keywords": ["Transfer Out", "manufacturing"], "task_order": 1} -->
#### Task: Use Transfer Out

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Transfer Out page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Transfer No Search:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Transfer Out, manufacturing

### Page: Vehicle

![Operation: Screen](screenshots/operation/operation.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation`

<!-- manual-meta: {"module": "Operation", "page": "Vehicle", "task": "Use Vehicle", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation", "screenshots": ["screenshots/operation/operation.png"], "keywords": ["Vehicle", "operation"], "task_order": 1} -->
#### Task: Use Vehicle

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Vehicle page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Vehicle No & Code:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Vehicle, operation

### Page: Price Declaration Wastage

![Price Declaration Wastage: Screen](screenshots/operation/price_declaration_wastage.png)

**Page purpose:** This page displays a list of wastage price declarations, showing validity dates, total quantities, and prices.

**Route:** `/operation/wastageManagement/priceDeclarationWastage`

<!-- manual-meta: {"module": "Operation", "page": "Price Declaration Wastage", "task": "View price declaration wastage list", "action": "view", "roles": [], "route": "/operation/wastageManagement/priceDeclarationWastage", "screenshots": ["screenshots/operation/price_declaration_wastage.png"], "keywords": ["wastage", "price declaration"], "task_order": 1} -->
#### Task: View price declaration wastage list

**Purpose:** To see the registered wastage price declaration records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Wastage Management module.

**Steps:**
1. Navigate to Operation > Wastage Management > Price Declaration Wastage.

**Fields and controls:**
* **SL:** Serial number of the entry.
* **Valid From Date:** Start date of the wastage price declaration.
* **Valid To Date:** End date of the wastage price declaration.
* **Total Qty.:** Total quantity of wastage items.
* **Total Price:** The total declared price value.

**Expected result:** A table showing current and historical wastage price declarations.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage, price declaration

### Page: Production

![Production: Screen](screenshots/operation/production.png)

![Production: Show](screenshots/operation/production_show.png)

**Page purpose:** This page allows users to view and search for production records within a selected branch and date range.

**Route:** `/operation/manufacturing/production`

<!-- manual-meta: {"module": "Operation", "page": "Production", "task": "Search production records", "action": "search", "roles": [], "route": "/operation/manufacturing/production", "screenshots": ["screenshots/operation/production.png", "screenshots/operation/production_show.png"], "keywords": ["production", "manufacturing", "filter"], "task_order": 1} -->
#### Task: Search production records

**Purpose:** To find specific production records by branch and date.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is authorized to view Manufacturing data.

**Steps:**
1. Navigate to Operation > Manufacturing > Production.
2. Select the Branch Name.
3. Enter or select the Form Date and To Date.
4. Click the View button.

**Fields and controls:**
* **Branch Name:** The specific branch to filter by.
* **Form Date:** Beginning of the search date range.
* **To Date:** End of the search date range.
* **Production No. Search:** Field to filter by a specific production number.

**Expected result:** A list of production entries matching the selected criteria will be displayed in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** production, manufacturing, filter

### Page: Purchase

![Purchase: Screen](screenshots/operation/purchase.png)

![Purchase: Show](screenshots/operation/purchase_show.png)

**Page purpose:** This page displays purchase invoice records and allows users to manage or search for them.

**Route:** `/operation/purchase/purchase`

<!-- manual-meta: {"module": "Operation", "page": "Purchase", "task": "View purchase list", "action": "view", "roles": [], "route": "/operation/purchase/purchase", "screenshots": ["screenshots/operation/purchase.png", "screenshots/operation/purchase_show.png"], "keywords": ["purchase", "invoice", "procurement"], "task_order": 1} -->
#### Task: View purchase list

**Purpose:** To review existing purchase invoices for a specific branch and time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the Purchase module.

**Steps:**
1. Navigate to Operation > Purchase > Purchase.
2. Select the branch from the Select Branch field.
3. Set the Enter From Date and Enter To Date.
4. Click View.

**Fields and controls:**
* **Select Branch:** The operational branch to view.
* **Enter From Date:** Start of the date filter.
* **Enter To Date:** End of the date filter.
* **BOE, BIN, Supplier Search:** Search input for specific invoices or suppliers.

**Expected result:** The purchase invoice table is populated with records matching the criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** purchase, invoice, procurement

### Page: Purchase

![Sales: Screen](screenshots/operation/sales.png)

![Sales: Show](screenshots/operation/sales_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/sales`

<!-- manual-meta: {"module": "Operation", "page": "Purchase", "task": "Use Purchase", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/sales", "screenshots": ["screenshots/operation/sales.png", "screenshots/operation/sales_show.png"], "keywords": ["Purchase", "sales"], "task_order": 1} -->
#### Task: Use Purchase

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Purchase page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.
* **BOE, BIN, Supplier Search:** Visible text control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Purchase, sales

### Page: Sales Invoice

![Sales Invoice: Screen](screenshots/operation/sales_invoice.png)

![Sales Invoice: Show](screenshots/operation/sales_invoice_show.png)

**Page purpose:** This page provides a search and display interface for all sales invoices recorded in the system.

**Route:** `/operation/sales/salesInvoice`

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "Search sales invoices", "action": "search", "roles": [], "route": "/operation/sales/salesInvoice", "screenshots": ["screenshots/operation/sales_invoice.png", "screenshots/operation/sales_invoice_show.png"], "keywords": ["sales", "invoice", "billing"], "task_order": 1} -->
#### Task: Search sales invoices

**Purpose:** To locate specific sales invoice records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to Sales module.

**Steps:**
1. Navigate to Operation > Sales > Sales Invoice.
2. Select a branch in the Select Branch field.
3. Define the period using the From Date and To Date pickers.
4. Click the View button.

**Fields and controls:**
* **Select Branch:** Filtering by branch.
* **From Date:** Beginning of the invoice date range.
* **To Date:** End of the invoice date range.
* **BOE, BIN, Inv No Search:** Find specific invoices by reference.

**Expected result:** Relevant sales invoices are shown in the table below.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoice, billing

### Page: Transfer In

![Transfer In: Screen](screenshots/operation/transfer_in.png)

![Transfer In: Show](screenshots/operation/transfer_in_show.png)

**Page purpose:** This page lists inventory items that have been transferred into the branch.

**Route:** `/operation/inventoryTransaction/transferIn`

<!-- manual-meta: {"module": "Operation", "page": "Transfer In", "task": "Filter transfer-in records", "action": "filter", "roles": [], "route": "/operation/inventoryTransaction/transferIn", "screenshots": ["screenshots/operation/transfer_in.png", "screenshots/operation/transfer_in_show.png"], "keywords": ["transfer", "inventory", "stock"], "task_order": 1} -->
#### Task: Filter transfer-in records

**Purpose:** To narrow down inventory transfers into the branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to Inventory Transaction.

**Steps:**
1. Navigate to Operation > Inventory Transaction > Transfer In.
2. Select the Branch Name.
3. Select the Item Type.
4. Click the View button.

**Fields and controls:**
* **Branch Name:** The target branch for the transfer-in.
* **Item Type:** Category of the inventory being transferred.
* **Transfer-In No Search:** Search by transfer number.

**Expected result:** Inventory Transfer-In records matching the selection are displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** transfer, inventory, stock

### Page: Transfer Out

![Transfer Out: Screen](screenshots/operation/transfer_out.png)

![Transfer Out: Show](screenshots/operation/transfer_out_show.png)

**Page purpose:** This page displays details of inventory transferred out from the current branch to another destination.

**Route:** `/operation/inventoryTransaction/transferOut`

<!-- manual-meta: {"module": "Operation", "page": "Transfer Out", "task": "View transfer-out details", "action": "view", "roles": [], "route": "/operation/inventoryTransaction/transferOut", "screenshots": ["screenshots/operation/transfer_out.png", "screenshots/operation/transfer_out_show.png"], "keywords": ["transfer", "outbound", "stock"], "task_order": 1} -->
#### Task: View transfer-out details

**Purpose:** To review the history and details of outgoing inventory transfers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Inventory Transaction module.

**Steps:**
1. Navigate to Operation > Inventory Transaction > Transfer Out.
2. Select the Branch Name.
3. Select the Item Type.
4. Click View.

**Fields and controls:**
* **Branch Name:** Source branch of the items.
* **Item Type:** The type of inventory items.
* **Transfer No Search:** Search by specific transfer record number.

**Expected result:** A table showing transfers to other locations including destination, address, vehicle info, and date.

**Warnings:**
* No specific warning was identified

**Search keywords:** transfer, outbound, stock

### Page: Wastage In

![Wastage In: Screen](screenshots/operation/wastage_in.png)

![Wastage In: Show](screenshots/operation/wastage_in_show.png)

**Page purpose:** This page allows users to view records of wastage brought into the facility.

**Route:** `/operation/wastageManagement/wastageIn`

<!-- manual-meta: {"module": "Operation", "page": "Wastage In", "task": "Search wastage in records", "action": "search", "roles": [], "route": "/operation/wastageManagement/wastageIn", "screenshots": ["screenshots/operation/wastage_in.png", "screenshots/operation/wastage_in_show.png"], "keywords": ["wastage", "waste", "management"], "task_order": 1} -->
#### Task: Search wastage in records

**Purpose:** To review records of incoming waste items.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Wastage Management module.

**Steps:**
1. Navigate to Operation > Wastage Management > Wastage In.
2. Select the Branch.
3. Specify the date range in From Date and To Date.
4. Click View.

**Fields and controls:**
* **Select Branch:** The branch where the wastage was received.
* **From Date:** Beginning of the record search period.
* **To Date:** End of the record search period.

**Expected result:** Records of incoming wastage items are displayed in the list.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage, waste, management

### Page: Sales Invoice

![Wastage Management: Screen](screenshots/operation/wastage_management.png)

![Wastage Management: Show](screenshots/operation/wastage_management_show.png)

**Page purpose:** Used to view and manage sales invoices under the wastage management module.

**Route:** `/operation/wastageManagement`

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "View Sales Invoices", "action": "view", "roles": [], "route": "/operation/wastageManagement", "screenshots": ["screenshots/operation/wastage_management.png", "screenshots/operation/wastage_management_show.png"], "keywords": ["sales", "invoice", "list", "view"], "task_order": 1} -->
#### Task: View Sales Invoices

**Purpose:** To list and review sales invoices within a specific date range and branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Operation module

**Steps:**
1. Navigate to Operation > Wastage Management
2. Select a branch from the Select Branch dropdown
3. Enter or select the From Date
4. Enter or select the To Date
5. Click the View button

**Fields and controls:**
* **Select Branch:** Dropdown to filter by business branch.
* **Enter From Date:** Start date for the invoice search.
* **Enter To Date:** End date for the invoice search.

**Expected result:** A table list of sales invoices matching the criteria will appear.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoice, list, view

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "Search Sales Invoices", "action": "search", "roles": [], "route": "/operation/wastageManagement", "screenshots": ["screenshots/operation/wastage_management.png", "screenshots/operation/wastage_management_show.png"], "keywords": ["search", "find", "BOE", "BIN"], "task_order": 2} -->
#### Task: Search Sales Invoices

**Purpose:** To find specific sales invoices using invoice identifiers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Operation module

**Steps:**
1. Navigate to Operation > Wastage Management
2. Enter a BOE, BIN, or Invoice Number in the search field
3. Click the search icon

**Fields and controls:**
* **BOE, BIN, Inv No Search:** Search input for specific document numbers.

**Expected result:** The table will update to show the matching invoice record.

**Warnings:**
* No specific warning was identified

**Search keywords:** search, find, BOE, BIN

### Page: Wastage Sales

![Wastage Sales: Screen](screenshots/operation/wastage_sales.png)

![Wastage Sales: Show](screenshots/operation/wastage_sales_show.png)

**Page purpose:** Used to view and manage sales invoices related to wastage operations.

**Route:** `/operation/wastageManagement/wastageSalesInvoice`

<!-- manual-meta: {"module": "Operation", "page": "Wastage Sales", "task": "View Wastage Sales", "action": "view", "roles": [], "route": "/operation/wastageManagement/wastageSalesInvoice", "screenshots": ["screenshots/operation/wastage_sales.png", "screenshots/operation/wastage_sales_show.png"], "keywords": ["wastage", "sales", "report"], "task_order": 1} -->
#### Task: View Wastage Sales

**Purpose:** To view the list of wastage sales records for a selected branch and period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is logged in
* Access to wastage sales module

**Steps:**
1. Navigate to Operation > Wastage Management > Wastage Sales
2. Select the branch
3. Select the date range using From Date and To Date fields
4. Click the View button

**Fields and controls:**
* **Select Branch:** Branch selector.
* **Enter From Date:** Beginning of the reporting period.
* **Enter To Date:** End of the reporting period.

**Expected result:** The wastage sales table will be populated with invoice data.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage, sales, report