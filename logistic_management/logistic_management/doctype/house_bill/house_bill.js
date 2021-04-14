// Copyright (c) 2021, Raj Tailot and contributors
// For license information, please see license.txt

frappe.ui.form.on('House Bill',{
    setup:function(frm) {
        console.log("here")
        // console.log(fr)
        frm.set_query("consignee_c",function(){
            return {
                filters :{
                    consignee: 1
                }
            };
        })
    },
   
    
   
});

frappe.ui.form.on('House Bill',{
    setup:function(frm){
        frm.set_query("shipper_c",function(){
            return {
                filters : {
                    shipper : 1
                }
            }
        });
    }
});

frappe.ui.form.on('House Bill',{
    setup:function(frm){
        frm.set_query("notify_c",function(){
            return{
                filters : {
                    notify : 1
                }
            }
        })
    }
})

frappe.ui.form.on('House Bill',{
    setup:function(frm){
        frm.set_query("agent",function(){
            return{
                filters : {
                    agent : 1
                }
            }
        })
    }
});





frappe.ui.form.on('House Bill', {
	refresh: function(frm) {
		if(frm.doc.shipment_channel != "Air"){
			var df = frappe.meta.get_docfield("Cargo Details","chargable_weight", frm.doc.name);
		df.read_only = 1
		
		frm.refresh_field("cargo_details")
		}
		


	}

});
cur_frm.fields_dict['sea_cargo_details'].grid.get_field('container').get_query = function(doc) {
	return {
		 filters: { 'container':doc.shipment },
		 query: "logistic_management.logistic_management.doctype.house_bill.house_bill.get_container_filter"
	}
}




 


