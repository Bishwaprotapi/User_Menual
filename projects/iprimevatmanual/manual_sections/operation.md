### Page: Contract Manufacturing Issue

![Contract Manufacturing Issue: Screen](screenshots/operation/contract_manufacturing_issue.png)

![Contract Manufacturing Issue: Show](screenshots/operation/contract_manufacturing_issue_show.png)

**Page purpose:** This page is used to manage and track the issuance of materials for contract manufacturing.

**Route:** `/operation/manufacturing/contactManufacturing`

<!-- manual-meta: {"module": "Operation", "page": "Contract Manufacturing Issue", "task": "Filter contract manufacturing issues", "action": "filter", "roles": [], "route": "/operation/manufacturing/contactManufacturing", "screenshots": ["screenshots/operation/contract_manufacturing_issue.png", "screenshots/operation/contract_manufacturing_issue_show.png"], "keywords": ["filter", "search", "contract", "issue", "manufacturing"], "task_order": 1} -->
#### Task: Filter contract manufacturing issues

**Purpose:** To view a list of specific contract manufacturing issue records within a selected time range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in.
* User must have access to the Operation module.

**Steps:**
1. Navigate to Operation > Manufacturing > Contract Manufacturing Issue.
2. Select the desired Branch.
3. Choose the From Date.
4. Choose the To Date.
5. Select the Issue Type.
6. Click the View button.

**Fields and controls:**
* **Branch:** The business location for the transaction.
* **From Date:** Start date of the search period.
* **To Date:** End date of the search period.
* **Issue Type:** The category of the material issue.

**Expected result:** The table displays the relevant contract manufacturing records based on the filters applied.

**Warnings:**
* No specific warning was identified

**Search keywords:** filter, search, contract, issue, manufacturing

### Page: Contract Manufacturing Receive

![Contract Manufacturing Receive: Screen](screenshots/operation/contract_manufacturing_receive.png)

![Contract Manufacturing Receive: Show](screenshots/operation/contract_manufacturing_receive_show.png)

**Page purpose:** This page is used to manage and view records of materials received from contract manufacturing.

**Route:** `/operation/manufacturing/contactMFGReceive`

<!-- manual-meta: {"module": "Operation", "page": "Contract Manufacturing Receive", "task": "Filter contract manufacturing receipts", "action": "filter", "roles": [], "route": "/operation/manufacturing/contactMFGReceive", "screenshots": ["screenshots/operation/contract_manufacturing_receive.png", "screenshots/operation/contract_manufacturing_receive_show.png"], "keywords": ["filter", "search", "receive", "manufacturing"], "task_order": 1} -->
#### Task: Filter contract manufacturing receipts

**Purpose:** To view a list of received material records from contract manufacturing within a specific date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in.
* User must have access to the Operation module.

**Steps:**
1. Navigate to Operation > Manufacturing > Contract Manufacturing Receive.
2. Select the desired Branch.
3. Choose the From Date.
4. Choose the To Date.
5. Select the Receive Type.
6. Click the View button.

**Fields and controls:**
* **Branch:** The business location for the transaction.
* **From Date:** Start date of the search period.
* **To Date:** End date of the search period.
* **Receive Type:** The category of the material received.

**Expected result:** The table displays the relevant contract manufacturing receipts based on the filters applied.

**Warnings:**
* No specific warning was identified

**Search keywords:** filter, search, receive, manufacturing

### Page: Credit Note

![Credit Note: Screen](screenshots/operation/credit_note.png)

**Page purpose:** This page provides a list of credit notes associated with sales invoices.

**Route:** `/operation/sales/credit-note`

<!-- manual-meta: {"module": "Operation", "page": "Credit Note", "task": "View credit notes", "action": "view", "roles": [], "route": "/operation/sales/credit-note", "screenshots": ["screenshots/operation/credit_note.png"], "keywords": ["credit", "note", "sales", "search"], "task_order": 1} -->
#### Task: View credit notes

**Purpose:** To view, search, or filter existing credit note records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in.

**Steps:**
1. Navigate to Operation > Sales > Credit Note.
2. Select the Branch.
3. Specify the date range using Form Date and To Date.
4. Use the Sales Invoice Search field to locate a specific note.
5. Click the View button to update the list.

**Fields and controls:**
* **Branch:** Selection of the business branch.
* **Form Date:** Start date filter for the report.
* **To Date:** End date filter for the report.
* **Sales Invoice Search:** Search by sales invoice number.

**Expected result:** A table populated with credit note data matching the search criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit, note, sales, search

### Page: Debit Note

![Debit Note: Screen](screenshots/operation/debit_note.png)

![Debit Note: Show](screenshots/operation/debit_note_show.png)

**Page purpose:** This page is used to manage and search for purchase-related debit notes.

**Route:** `/operation/purchase/debit-note`

<!-- manual-meta: {"module": "Operation", "page": "Debit Note", "task": "Search for debit notes", "action": "search", "roles": [], "route": "/operation/purchase/debit-note", "screenshots": ["screenshots/operation/debit_note.png", "screenshots/operation/debit_note_show.png"], "keywords": ["debit", "note", "purchase", "search"], "task_order": 1} -->
#### Task: Search for debit notes

**Purpose:** To find specific debit notes associated with purchase invoices.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in.

**Steps:**
1. Navigate to Operation > Purchase > Debit Note.
2. Select the Branch Name.
3. Enter the Form Date and To Date.
4. Enter a keyword in the Purchase Invoice Search field.
5. Click View to apply the filters.

**Fields and controls:**
* **Branch Name:** The business entity or branch.
* **Purchase Invoice Search:** Lookup field for purchase invoices.

**Expected result:** The list of debit notes matching the provided invoice search and date criteria appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit, note, purchase, search

### Page: User Profile

![Inventory Transaction: Screen](screenshots/operation/inventory_transaction.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/inventoryTransaction`

<!-- manual-meta: {"module": "Operation", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/inventoryTransaction", "screenshots": ["screenshots/operation/inventory_transaction.png"], "keywords": ["User Profile", "inventory transaction"], "task_order": 1} -->
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

**Search keywords:** User Profile, inventory transaction

### Page: Item Destroy

![Item Destroy: Screen](screenshots/operation/item_destroy.png)

![Item Destroy: Show](screenshots/operation/item_destroy_show.png)

**Page purpose:** This page is used to track and view records of items that have been destroyed or removed from inventory.

**Route:** `/operation/inventoryTransaction/itemDestroy`

<!-- manual-meta: {"module": "Operation", "page": "Item Destroy", "task": "Filter destroyed items", "action": "filter", "roles": [], "route": "/operation/inventoryTransaction/itemDestroy", "screenshots": ["screenshots/operation/item_destroy.png", "screenshots/operation/item_destroy_show.png"], "keywords": ["inventory", "destroy", "wastage"], "task_order": 1} -->
#### Task: Filter destroyed items

**Purpose:** To list items that have been destroyed within a specified date range and type.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in.

**Steps:**
1. Navigate to Operation > Inventory Transaction > Item Destroy.
2. Select the Branch Name.
3. Define the From Date and To Date.
4. Select the Item Type.
5. Click View.

**Fields and controls:**
* **Branch Name:** The business location for the transaction.
* **Item Type:** The category of item to view.

**Expected result:** A list of destroyed item records that match the selected parameters.

**Warnings:**
* No specific warning was identified

**Search keywords:** inventory, destroy, wastage

### Page: User Profile

![Manufacturing: Screen](screenshots/operation/manufacturing.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/manufacturing`

<!-- manual-meta: {"module": "Operation", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/manufacturing", "screenshots": ["screenshots/operation/manufacturing.png"], "keywords": ["User Profile", "manufacturing"], "task_order": 1} -->
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

**Search keywords:** User Profile, manufacturing

### Page: User Profile

![Operation: Screen](screenshots/operation/operation.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation`

<!-- manual-meta: {"module": "Operation", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation", "screenshots": ["screenshots/operation/operation.png"], "keywords": ["User Profile", "operation"], "task_order": 1} -->
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

**Search keywords:** User Profile, operation

### Page: Price Declaration Wastage

![Price Declaration Wastage: Screen](screenshots/operation/price_declaration_wastage.png)

**Page purpose:** This page allows users to view and manage price declarations for wastage.

**Route:** `/operation/wastageManagement/priceDeclarationWastage`

<!-- manual-meta: {"module": "Operation", "page": "Price Declaration Wastage", "task": "View Price Declaration Wastage", "action": "view", "roles": [], "route": "/operation/wastageManagement/priceDeclarationWastage", "screenshots": ["screenshots/operation/price_declaration_wastage.png"], "keywords": ["price declaration", "wastage", "price list"], "task_order": 1} -->
#### Task: View Price Declaration Wastage

**Purpose:** To view the list of declared wastage prices and their validity periods.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Wastage Management > Price Declaration Wastage.
2. Review the list of records in the table.
3. Use the 'Rows per page' dropdown to adjust the number of visible entries if necessary.

**Fields and controls:**
* **SL:** Serial number of the entry.
* **Valid From Date:** The start date for the price declaration.
* **Valid To Date:** The end date for the price declaration.
* **Total Qty.:** The quantity associated with the wastage price.
* **Total Price:** The declared price for the wastage.

**Expected result:** A table displaying existing price declaration records.

**Warnings:**
* No specific warning was identified

**Search keywords:** price declaration, wastage, price list

### Page: Production

![Production: Screen](screenshots/operation/production.png)

![Production: Show](screenshots/operation/production_show.png)

**Page purpose:** This page allows users to track and view production records for selected branches.

**Route:** `/operation/manufacturing/production`

<!-- manual-meta: {"module": "Operation", "page": "Production", "task": "Search Production Records", "action": "search", "roles": [], "route": "/operation/manufacturing/production", "screenshots": ["screenshots/operation/production.png", "screenshots/operation/production_show.png"], "keywords": ["manufacturing", "production report", "factory output"], "task_order": 1} -->
#### Task: Search Production Records

**Purpose:** To filter production records by branch and date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Manufacturing > Production.
2. Select the 'Branch Name'.
3. Enter the 'Form Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Branch Name:** The branch where the production occurred.
* **Form Date:** Starting date filter.
* **To Date:** Ending date filter.
* **Production No. Search:** Direct search by production number.

**Expected result:** A list of production records matching the selected branch and date criteria will be displayed in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** manufacturing, production report, factory output

### Page: Purchase

![Purchase: Screen](screenshots/operation/purchase.png)

![Purchase: Show](screenshots/operation/purchase_show.png)

**Page purpose:** This page provides an overview of purchase transactions.

**Route:** `/operation/purchase/purchase`

<!-- manual-meta: {"module": "Operation", "page": "Purchase", "task": "Filter Purchase Invoices", "action": "filter", "roles": [], "route": "/operation/purchase/purchase", "screenshots": ["screenshots/operation/purchase.png", "screenshots/operation/purchase_show.png"], "keywords": ["purchase history", "vendor invoices", "procurement"], "task_order": 1} -->
#### Task: Filter Purchase Invoices

**Purpose:** To find specific purchase invoices for a specific branch and date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Purchase > Purchase.
2. Select the 'Select Branch'.
3. Define the 'Enter From Date' and 'Enter To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Select Branch:** The branch context for the purchase.
* **Enter From Date:** Start date for filtering.
* **Enter To Date:** End date for filtering.
* **BOE, BIN, Supplier Search:** Search by Bill of Entry, Business Identification Number, or Supplier name.

**Expected result:** The table will populate with relevant purchase invoices based on the selected filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** purchase history, vendor invoices, procurement

### Page: User Profile

![Sales: Screen](screenshots/operation/sales.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/sales`

<!-- manual-meta: {"module": "Operation", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/sales", "screenshots": ["screenshots/operation/sales.png"], "keywords": ["User Profile", "sales"], "task_order": 1} -->
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

**Search keywords:** User Profile, sales

### Page: Sales Invoice

![Sales Invoice: Screen](screenshots/operation/sales_invoice.png)

![Sales Invoice: Show](screenshots/operation/sales_invoice_show.png)

**Page purpose:** This page allows users to view and manage sales invoices.

**Route:** `/operation/sales/salesInvoice`

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "Filter Sales Invoices", "action": "filter", "roles": [], "route": "/operation/sales/salesInvoice", "screenshots": ["screenshots/operation/sales_invoice.png", "screenshots/operation/sales_invoice_show.png"], "keywords": ["invoices", "sales history", "billing"], "task_order": 1} -->
#### Task: Filter Sales Invoices

**Purpose:** To locate sales invoices generated within a specific timeframe for a branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Sales > Sales Invoice.
2. Select the 'Select Branch'.
3. Input the 'Enter From Date' and 'Enter To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Select Branch:** The branch where the sale occurred.
* **Enter From Date:** Start of the date range.
* **Enter To Date:** End of the date range.
* **BOE, BIN, Inv No Search:** Search field to refine by identifier.

**Expected result:** The table displays matching sales invoice records.

**Warnings:**
* No specific warning was identified

**Search keywords:** invoices, sales history, billing

### Page: Item Transfer-In

![Transfer In: Screen](screenshots/operation/transfer_in.png)

![Transfer In: Show](screenshots/operation/transfer_in_show.png)

**Page purpose:** This page displays all incoming item transfers into a specific branch.

**Route:** `/operation/inventoryTransaction/transferIn`

<!-- manual-meta: {"module": "Operation", "page": "Item Transfer-In", "task": "View Incoming Transfers", "action": "view", "roles": [], "route": "/operation/inventoryTransaction/transferIn", "screenshots": ["screenshots/operation/transfer_in.png", "screenshots/operation/transfer_in_show.png"], "keywords": ["inbound inventory", "stock transfer", "logistics"], "task_order": 1} -->
#### Task: View Incoming Transfers

**Purpose:** To see incoming inventory movements.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Inventory Transaction > Transfer In.
2. Select the 'Branch Name'.
3. Select the 'Item Type'.
4. Click 'View'.

**Fields and controls:**
* **Branch Name:** Target branch for the transfer.
* **Item Type:** Type of inventory being transferred.

**Expected result:** A table showing details of the transfer, such as date, transfer number, and origin branch.

**Warnings:**
* No specific warning was identified

**Search keywords:** inbound inventory, stock transfer, logistics

### Page: Transfer Out

![Transfer Out: Screen](screenshots/operation/transfer_out.png)

![Transfer Out: Show](screenshots/operation/transfer_out_show.png)

**Page purpose:** This page manages outbound inventory transfers between branches.

**Route:** `/operation/inventoryTransaction/transferOut`

<!-- manual-meta: {"module": "Operation", "page": "Transfer Out", "task": "View Outbound Transfers", "action": "view", "roles": [], "route": "/operation/inventoryTransaction/transferOut", "screenshots": ["screenshots/operation/transfer_out.png", "screenshots/operation/transfer_out_show.png"], "keywords": ["outbound stock", "shipment", "inventory movement"], "task_order": 1} -->
#### Task: View Outbound Transfers

**Purpose:** To monitor inventory sent to other locations.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Inventory Transaction > Transfer Out.
2. Select the 'Branch Name'.
3. Select the 'Item Type'.
4. Click 'View'.

**Fields and controls:**
* **Branch Name:** The branch initiating the transfer.
* **Item Type:** Category of inventory to view.
* **Transfer No Search:** Search by transfer document number.

**Expected result:** A list of outbound transfer records is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** outbound stock, shipment, inventory movement

### Page: Wastage In

![Wastage In: Screen](screenshots/operation/wastage_in.png)

![Wastage In: Show](screenshots/operation/wastage_in_show.png)

**Page purpose:** This page is used to manage and view incoming wastage records.

**Route:** `/operation/wastageManagement/wastageIn`

<!-- manual-meta: {"module": "Operation", "page": "Wastage In", "task": "List Wastage In Records", "action": "filter", "roles": [], "route": "/operation/wastageManagement/wastageIn", "screenshots": ["screenshots/operation/wastage_in.png", "screenshots/operation/wastage_in_show.png"], "keywords": ["scrap management", "wastage report", "inventory damage"], "task_order": 1} -->
#### Task: List Wastage In Records

**Purpose:** To retrieve and view records of incoming wastage within a date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Operation > Wastage Management > Wastage In.
2. Select the 'Select Branch'.
3. Set the 'Enter From Date' and 'Enter To Date'.
4. Click 'View'.

**Fields and controls:**
* **Select Branch:** Branch where wastage was recorded.
* **Enter From Date:** Start date for reporting.
* **Enter To Date:** End date for reporting.

**Expected result:** The wastage records will appear in the result table.

**Warnings:**
* No specific warning was identified

**Search keywords:** scrap management, wastage report, inventory damage

### Page: User Profile

![Wastage Management: Screen](screenshots/operation/wastage_management.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/wastageManagement`

<!-- manual-meta: {"module": "Operation", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/wastageManagement", "screenshots": ["screenshots/operation/wastage_management.png"], "keywords": ["User Profile", "wastage management"], "task_order": 1} -->
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

**Search keywords:** User Profile, wastage management

### Page: Wastage Sales

![Wastage Sales: Screen](screenshots/operation/wastage_sales.png)

![Wastage Sales: Show](screenshots/operation/wastage_sales_show.png)

**Page purpose:** This page allows users to view, search, and manage records related to the sales of wastage items.

**Route:** `/operation/wastageManagement/wastageSalesInvoice`

<!-- manual-meta: {"module": "Operation", "page": "Wastage Sales", "task": "View wastage sales records", "action": "view", "roles": [], "route": "/operation/wastageManagement/wastageSalesInvoice", "screenshots": ["screenshots/operation/wastage_sales.png", "screenshots/operation/wastage_sales_show.png"], "keywords": ["wastage invoice", "sales history", "view wastage"], "task_order": 1} -->
#### Task: View wastage sales records

**Purpose:** To list and monitor existing wastage sales transactions within a specific branch and time frame.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in.
* Wastage sales records must exist for the selected branch and date range.

**Steps:**
1. Navigate to Operation > Wastage Management > Wastage Sales.
2. Select the desired branch from the 'Select Branch' dropdown.
3. Choose a start date in the 'Enter From Date' field.
4. Choose an end date in the 'Enter To Date' field.
5. Click the 'View' button.

**Fields and controls:**
* **Select Branch:** Dropdown to filter records by company branch.
* **Enter From Date:** Start date for the report range.
* **Enter To Date:** End date for the report range.

**Expected result:** A table populated with wastage sales records matching the search criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage invoice, sales history, view wastage

<!-- manual-meta: {"module": "Operation", "page": "Wastage Sales", "task": "Search wastage sales", "action": "search", "roles": [], "route": "/operation/wastageManagement/wastageSalesInvoice", "screenshots": ["screenshots/operation/wastage_sales.png", "screenshots/operation/wastage_sales_show.png"], "keywords": ["find invoice", "search wastage", "filter records"], "task_order": 2} -->
#### Task: Search wastage sales

**Purpose:** To quickly locate specific wastage sales records using invoice or identifier details.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be on the Wastage Sales page.

**Steps:**
1. Navigate to the search bar labeled 'BOE, BIN, Inv No Search'.
2. Enter the BOE (Bill of Export), BIN (Business Identification Number), or Invoice Number.
3. Click the search icon.

**Fields and controls:**
* **BOE, BIN, Inv No Search:** Input field to filter results by specific document numbers.

**Expected result:** The table displays only records corresponding to the entered search term.

**Warnings:**
* No specific warning was identified

**Search keywords:** find invoice, search wastage, filter records