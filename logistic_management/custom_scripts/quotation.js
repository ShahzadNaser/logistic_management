
frappe.ui.form.on('Quotation', {
    refresh: function(frm) {
        cur_frm.add_custom_button(__('Shipment'), function() {
            console.log("here")
            frappe.model.open_mapped_doc({
            method: "logistic_management.logistic_management.quotation.create_shipment",
            frm: cur_frm
            })
        },__("Create"))
    },

})

frappe.ui.form.on('Quotation Item', {
	refresh(frm) {
		// your code here
	},
	on_actual(frm,cdt,cdn){
	    var row = locals[cdt][cdn]
	    if(row.on_actual){
	        row.rate = 0.00
	        cur_frm.script_manager.trigger("rate", row.doctype, row.name);
	        frm.refresh_field("items")
	    }
	}
})