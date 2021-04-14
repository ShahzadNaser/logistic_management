// Copyright (c) 2021, Raj Tailot and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shipment Job Master', {
	refresh(frm) {
		// your code here
	},
	port_of_loading_a:function(frm){
	    if(frm.doc.port_of_loading_a && frm.doc.port_of_destination_a){
	        if(frm.doc.port_of_loading_a == frm.doc.port_of_destination_a){
	            frappe.throw("Port Of Loading And Port Of Destination Can Not Be Same !")
	        }
	    }
	    
	},
	port_of_destination_a:function(frm){
	    frm.trigger("port_of_loading_a")
	}
})


frappe.ui.form.on('Shipment Job Master', {
	refresh(frm) {
		// your code here
	},
	pol:function(frm){
	    if(frm.doc.pol && frm.doc.pod){
	        if(frm.doc.pol == frm.doc.pod){
	            frappe.throw("Port Of Loading And Port Of Destination Can Not Be Same !")
	        }
	    }
	    
	},
	pod:function(frm){
	    frm.trigger("pol")
	}
})

frappe.ui.form.on('Shipment Job Master', {
	refresh(frm) {
		// your code here
	},
	port_of_loading:function(frm){
	    if(frm.doc.port_of_loading && frm.doc.port_of_destination){
	        if(frm.doc.port_of_loading == frm.doc.port_of_destination){
	            frappe.throw("Port Of Loading And Port Of Destination Can Not Be Same !")
	        }
	    }
	    
	},
	port_of_destination:function(frm){
	    frm.trigger("port_of_loading")
	}
})


frappe.ui.form.on('Shipment Job Master', {
	refresh(frm) {
		// your code here
	},
	airport_of_loading:function(frm){
	    if(frm.doc.airport_of_loading && frm.doc.airport_of_destination){
	        if(frm.doc.airport_of_loading == frm.doc.airport_of_destination){
	            frappe.throw("Port Of Loading And Port Of Destination Can Not Be Same !")
	        }
	    }
	    
	},
	airport_of_destination:function(frm){
	    frm.trigger("airport_of_loading")
	}
	
	
})

frappe.ui.form.on('Shipment Job Master', {
     mawb_no:function(frm){
     var value = frm.doc.mawb_no;
     var pattern = new RegExp("^[0-9]{8,8}$");
     if(!pattern.test(value)){
         frappe.throw("Pattern Not Matching Valid Only For 8 Digits");
     }
    
     var result = pattern.test(value);
     console.log(result);
 //The rest of your code. :)
}
});
frappe.ui.form.on('Shipment Job Master', {
	job_type:function(frm) {
	    if(frm.doc.shipment_channel){
			if(frm.doc.shipment_channel == "Air"){
				frm.set_value("job_type","AF")
				frm.refresh_field("job_type")
			}if(frm.doc.shipment_channel == "Sea"){
				frm.set_value("job_type","SF")
				frm.refresh_field("job_type")
			}
			if(frm.doc.shipment_channel == "Land"){
				frm.set_value("job_type","CF")
				frm.refresh_field("job_type")
			}
			if(frm.doc.shipment_channel == "Courier"){
				frm.set_value("job_type","CF")
				frm.refresh_field("job_type")
			}

		}
	}
});
