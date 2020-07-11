from api.models.case_Info import Purchase,Case_cigar,Brand,ExcelInAndOut
from api.models.store_Info import Store

purchase_info_ser = [
    Purchase.id,
    Purchase.store_id,
    Store.store_name,
    Purchase.purchase_date,
    Purchase.purchase_week,
    Purchase.settlement_account,
    Purchase.required_count,
    Purchase.average_price
]

casecigar_info_ser = [
    Case_cigar.id,
    Case_cigar.case_id,
    Case_cigar.store_name,
    Case_cigar.business_number,
    Case_cigar.case_date,
    Case_cigar.case_nature,
    Case_cigar.cigar_property,
    Case_cigar.singlebrandname,
    Case_cigar.count,
    Case_cigar.cigar_codefront,
    Case_cigar.cigar_codebehind,
    Case_cigar.origin_area
]

brand_info_ser = [
    Brand.id,
    Brand.purchase_id,
    Brand.cigar_name,
    Brand.cigar_price,
    Brand.cigar_num
]

brand_info_ser = [
    Brand.id,
    Brand.purchase_id,
    Brand.cigar_name,
    Brand.cigar_price,
    Brand.cigar_num
]

excel_inandout_info_ser = [
    ExcelInAndOut.id,
    ExcelInAndOut.input_caseid,
    ExcelInAndOut.singlebrand_id,
    ExcelInAndOut.singlebrand_name,
    ExcelInAndOut.code_front,
    ExcelInAndOut.code_behind,
    ExcelInAndOut.count
]