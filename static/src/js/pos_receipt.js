odoo.define('custom_pos_javascript_file.receipt', function (require) {
"use strict";
   var { Orderline } = require('point_of_sale.models');
   var Registries = require('point_of_sale.Registries');
   const CustomOrder = (Orderline) => class CustomOrder extends Orderline {
       export_for_printing() {
       var result = super.export_for_printing(...arguments);
       var rating = this.product.rating
       result.rating = ''

       let i='';
       let j=0;

       while (j < rating){
       i = '\u2605';
       j++;
       result.rating += i
       }
       return result;
   }
   }
       Registries.Model.extend(Orderline, CustomOrder);
   });