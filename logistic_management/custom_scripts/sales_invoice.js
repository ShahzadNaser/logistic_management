frappe.ui.form.on('Sales Invoice', {
    branch:function(frm) {
     if(frm.doc.branch == "Dammam Logistics"){
        frm.set_value("naming_series","DL.YY.-")
        frm.refresh_field("naming_series")
     }else if(frm.doc.branch == "Jeddah Logistics"){
        frm.set_value("naming_series","JL.YY.-")
        frm.refresh_field("naming_series")
     }   
    },
	house_bill:function(frm) {
	    frappe.db.get_value("Shipment Job Master",frm.doc.job_no_c,"shipment_type").then((res)=>{
	       // console.log(res)
	        if(res.message){
	            var house_bill = frappe.get_doc("House Bill",frm.doc.house_bill)
	           // console.log(house_bill)
	            if(res.message.shipment_type == "Export"){
	                frm.set_value("customer",house_bill.shipper_c)
	            }else{
	                frm.set_value("customer",house_bill.consignee_)
	            }
	            frm.refresh_field("customer")
	        }
	    })
	}

});


frappe.ui.form.on('Sales Invoice Item', {
	refresh(frm) {
		// your code here
	},
	rate_custom(frm,cdt,cdn){
	    var row = locals[cdt][cdn]
	  frappe.call({
			method: "erpnext.setup.utils.get_exchange_rate",
			args: {
				
				from_currency: row.currency_c,
				to_currency: frm.doc.price_list_currency
			},
			callback: function(r) {
				console.log(r)
				var ex = r.message
				row.rate = row.rate_custom * ex
				row.exchange_rate_custom = r.message
				frm.refresh_field("items")
			}
	      
	  })  
	},
	currency_c(frm,cdt,cdn){
	    var row = locals[cdt][cdn]
	    cur_frm.script_manager.trigger("rate_custom", row.doctype, row.name);
	},
	exchange_rate_custom(frm,cdt,cdn){
	    var row = locals[cdt][cdn]
	    cur_frm.script_manager.trigger("rate_custom", row.doctype, row.name);
	}
	
})