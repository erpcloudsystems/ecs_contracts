// Copyright (c) 2021, ERP Cloud Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lease Contract', 'contract_period',  function(frm) {
    if(cur_frm.doc.contract_period == "Months"){
        cur_frm.set_value('no_of_months', '');
        cur_frm.set_value('no_of_years', '');
    }
});

frappe.ui.form.on("Lease Contract", "no_of_years", function(frm){
    var x = cur_frm.doc.no_of_years * 12;
    cur_frm.set_value("no_of_months",x);
});

frappe.ui.form.on("Lease Contract","validate", function(frm){
    if(cur_frm.doc.no_of_months <= 0){
        frappe.throw("Please Enter No Of Months");
    }
    if(cur_frm.doc.contract_period == "Years" && cur_frm.doc.no_of_years <= 0){
        frappe.throw("Please Enter No Of Years");
    }
    if(cur_frm.doc.no_of_months > 240){
        frappe.throw("Maximum Contract Length Is 20 Years");
    }
});

frappe.ui.form.on("Lease Contract","party_type", function(frm){
    cur_frm.set_value("party","");
    cur_frm.set_value("party_name","");
});

frappe.ui.form.on('Lease Contract', 'party',  function(frm) {

    if (cur_frm.doc.party_type =="Customer"){

    frappe.call({ method: "frappe.client.get_value",
	args: { doctype: "Customer",
	fieldname: "customer_name",
	filters: { 'name': cur_frm.doc.party},
	}, callback: function(r)
	{cur_frm.set_value("party_name", r.message.customer_name);
  } });
        }

  if (cur_frm.doc.party_type =="Supplier"){

    frappe.call({ method: "frappe.client.get_value",
    args: { doctype: "Supplier",
    fieldname: "supplier_name",
    filters: { 'name': cur_frm.doc.party},
    }, callback: function(r)
    {cur_frm.set_value("party_name", r.message.supplier_name);
  } });
        }
});

frappe.ui.form.on("Contract Repayment Schedule", "make_payment", function(frm,cdt,cdn) {
{
                frappe.db.insert(populate_je_obj(frm))
                    .then(function (doc) {
                        console.log(`${doc.doctype} ${doc.name} created on ${doc.creation}`);
                        frappe.set_route('Form', doc.doctype, doc.name);

                        }
                );
}
    function populate_je_obj(frm, data) {
	var d = locals[cdt][cdn];
    let je = {};
    let accounts = [
                {
                    "doctype": "Journal Entry Account",
                    "account": frm.doc.rental_expense_account,
                    "debit": d.monthly_payment,
                    "credit": 0,
                    "debit_in_account_currency": d.monthly_payment,
                    "user_remark": cur_frm.docname
                },
                {
                    "doctype": "Journal Entry Account",
                    "account": frm.doc.cash_account,
                    "debit": 0,
                    "credit": d.monthly_payment,
                    "credit_in_account_currency": d.monthly_payment,
                    "user_remark": cur_frm.docname
                },

            ];

    je["doctype"] = "Journal Entry";
    je["voucher_type"] = "Journal Entry";
    je["reference_doctype"] = "Lease Contract";
    je["reference_link"] = cur_frm.doc.name;
    je["cheque_no"] = cur_frm.doc.name;
    je["bill_no"] = d.name;

    je["cheque_date"] = d.payment_date;
    je["posting_date"] = d.payment_date;

    je["accounts"] = accounts;
    return je;

}
function submit_je(frm) {
    ccco_params.je["remark"] = cur_frm.docname;
    frappe.db.insert(ccco_params.je)
        .then(function (doc) {
            frappe.call({
                "method": "frappe.client.submit",
                "args": {
                    "doc": doc
                },
                "callback": (r) => {
                    console.log(r);
                }
            });
        });
}
});


