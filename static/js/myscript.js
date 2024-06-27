
  
$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2]
    console.log("pid",id)
    $.ajax{{
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        }
        success:function(data){
            console.log("data =",data);
            em1.innerText=data.product_qty
            document.getElementId("amount").innerText=data.amount
            document.getElementId("totalamount").innerText=data.totalamount
        }
    }}
   })