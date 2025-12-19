import sys

# SAP T-Code Mapper Tool
# A simple script to search for SAP transaction codes and their descriptions.

TCODE_DB = {
    # System & General
    "/N": "System: Back to main menu.",
    "/O": "System: Open new session.",
    "/NEX": "System: Log off all sessions.",
    
    # Developers (ABAP)
    "SE11": "ABAP Dictionary - Data definitions and table maintenance.",
    "SE38": "ABAP Editor - Create and edit reports.",
    "SE80": "Object Navigator - Integrated development environment.",
    "SE37": "Function Builder - Manage function modules.",
    "SE24": "Class Builder - Object-Oriented ABAP development.",
    "SE16N": "General Table Display - View database table contents.",
    "ST22": "ABAP Dump Analysis - Diagnostic tool for runtime errors.",
    "SM30": "Call View Maintenance - Maintain table entries.",
    "SE71": "SAPscript Form Painter.",
    "SFP": "SAP Interactive Forms by Adobe.",
    
    # Finance (FI)
    "FB01": "Post Document - General accounting entry.",
    "FBL3N": "G/L Account Line Item Display.",
    "FS00": "G/L Account Master Record maintenance.",
    "FB50": "G/L Document Post (Enjoy Transaction).",
    "FB60": "Enter Incoming Invoices (Vendors).",
    "FB70": "Enter Outgoing Invoices (Customers).",
    "F110": "Parameters for Automatic Payment.",
    "AS01": "Create Asset Master Record.",
    "AFAB": "Post Depreciation Run.",
    
    # Controlling (CO)
    "KS01": "Create Cost Center.",
    "KOK5": "Cost Center List.",
    "KO01": "Create Internal Order.",
    
    # Materials Management (MM)
    "MM01": "Create Material - Register new goods or services.",
    "MM02": "Change Material.",
    "MM03": "Display Material.",
    "MMBE": "Stock Overview.",
    "ME21N": "Create Purchase Order.",
    "ME23N": "Display Purchase Order.",
    "MIGO": "Goods Movement - Receive or transfer stock.",
    "MIRO": "Enter Incoming Invoice - Verify vendor invoices.",
    "MD04": "Stock/Requirements List.",
    
    # Sales and Distribution (SD)
    "VA01": "Create Sales Order.",
    "VA02": "Change Sales Order.",
    "VA03": "Display Sales Order.",
    "VL01N": "Create Outbound Delivery.",
    "VF01": "Create Billing Document.",
    "XD01": "Create Customer Master.",
    
    # Production Planning (PP)
    "MD01": "MRP Run.",
    "CO01": "Create Production Order.",
    "CS01": "Create Bill of Material (BOM).",
    
    # Basis & Administration
    "SU01": "User Maintenance - Manage user accounts.",
    "SU10": "User Mass Maintenance.",
    "PFCG": "Role Maintenance - Manage permissions.",
    "SM04": "User Overview - Monitor active sessions.",
    "AL08": "Users Logged On - Global overview.",
    "STMS": "Transport Management System.",
    "SM37": "Background Job Overview.",
    "SM21": "System Log Analysis.",
    "SCOT": "SAPconnect - SAP Mail / Fax configuration."
}

def search_tcode(query):
    query = query.upper()
    print(f"\n🔍 Searching for: {query}\n" + "-"*30)
    
    found = False
    for code, desc in TCODE_DB.items():
        if query in code or query in desc.upper():
            print(f"✅ [{code}]: {desc}")
            found = True
            
    if not found:
        print("❌ No matching Transaction Code found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_tcode(" ".join(sys.argv[1:]))
    else:
        print("Usage: python tcode_mapper.py <T-Code or Description>")
        print("Example: python tcode_mapper.py MM01")
