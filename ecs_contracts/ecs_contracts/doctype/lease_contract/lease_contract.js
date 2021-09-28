// Copyright (c) 2021, ERP Cloud Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Lease Contract","no_of_years", function(frm){
    var x = cur_frm.doc.no_of_years * 12;
        cur_frm.set_value("no_of_months",x);
});

frappe.ui.form.on("Lease Contract","validate", function(frm){
    if(cur_frm.doc.no_of_months > 11 && cur_frm.doc.contract_period == "Less Than 1 Year"){
        frappe.throw("No Of Months Should Be Less Than 12");
    }
});
