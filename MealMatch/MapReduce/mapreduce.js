/**
 * Created by Axel on 2017-04-05.
 */


var mapfunction = function() {
    var value = {};
    var array = [];

    for (var index = 0; index < this.ingredients_list.length; index++){
        var key = this.ingredients_list[index];
        //value[this._id] = this.title;


        value[this.title] = this._id

        emit(key, value)


    }
}

var reducefunction = function (ing, title) {
    var result = {};
    title.forEach(function(title) {
        for (var id in title) {
            result[id] = title[id];
            //result[title] = title[title]
        }
    });
    return result;

}

var finalizefunc= function (key, result ){
    var array = []


    //Look up scope function
    for (var key in result){


        array.push(result[key])

    }



    return array

}


//}
    //var arr = title.toString()
    //return title




db.recipe.mapReduce(
    mapfunction,
    reducefunction,
    { out: "mapped",
    finalize: finalizefunc}


)

db.mapped.aggregate(
    [
        { "$addFields": {
            "title": { "$concat": ["$_id"] }
        }},
        { "$out": "mapped" }
    ]
)



//reduce = function(key, values) {
  //var result = {};
  //values.forEach(function(value) {
    //for (var id in value) {
      // result[id] = value[id];
    //}
  //});
  //return result;
//}