import sys

# SAP T-Code Mapper Tool
# A simple script to search for SAP transaction codes and their descriptions.

TCODE_DB = {
    # General
    "SE11": "ABAP Dictionary - Data definitions and table maintenance.",
    "SE38": "ABAP Editor - Create and edit reports.",
    "SE80": "Object Navigator - Integrated development environment.",
    "SU01": "User Maintenance - Manage user accounts and roles.",
    "SM04": "User Overview - Monitor active sessions.",
    
    # Finance (FI)
    "FB01": "Post Document - General accounting entry.",
    "FBL3N": "G/L Account Line Item Display.",
    "FS00": "G/L Account Master Record maintenance.",
    
    # Materials Management (MM)
    "MM01": "Create Material - Register new goods or services.",
    "ME21N": "Create Purchase Order - Ordering materials from vendors.",
    "MIGO": "Goods Movement - Receive or transfer stock.",
    "MIRO": "Enter Incoming Invoice - Verify vendor invoices.",
    
    # Sales and Distribution (SD)
    "VA01": "Create Sales Order - Customer order entry.",
    "VL01N": "Create Outbound Delivery - Prepare items for shipping.",
    "VF01": "Create Billing Document - Generating customer invoices.",
    
    # Production Planning (PP)
    "MD04": "Stock/Requirements List - Production planning status.",
    "CO01": "Create Production Order - Initiate manufacturing process."
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
