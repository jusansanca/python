/* const http = require('http');
const uc = require('upper-case');

http.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'}); ///200 es el ocdigo de las operaciones exitosas en internet
    res.write(uc.upperCase('Hola NODEJS'));
    res.end();
}).listen(8080); */

const { rejects } = require("assert");
const { resolve } = require("path");

/* const fs = require('fs');
const rs = fs.createReadStream('./demofile.txt');
rs.on('open', function(){
    console-console.log('The File is Open')
}); */

/* const events = require('events');
const eventEmitter = new events.EventEmitter();

//create an event handler:
const myEventHandler = function(){
    console.log('I hear a scream!');
}

//assign the event handler to an event:
eventEmitter.on('scream', myEventHandler);

//fire the 'scream' event:
eventEmitter.emit('scream');
 */

//upload file

/* const http = require('http');
const formidable = require('formidable');
const fs = require('fs'); 

http.createServer(function(req, res){
    if (req.url == '/fileupload') {
        const form = new formidable.IncomingForm();
        form.parse(req, function(err, fields, files){
            let oldpath = files.filetoupload.filepath;
            let newpath = 'C:/xampp/python_jssc/NODEJS/' + files.filetoupload.originalFilename;
            fs.rename(oldpath, newpath, function (err){
                if (err) throw err;
                res.write('File uploaded');
                res.end();
            });
    });
    }else {
        res.writeHead(200,{'Content-Type':'text/html'});
        res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
        res.write('<input type="file" name="filetoupload"><br>');
        res.write('<input type="submit" value="Enviar">');
        res.write('</form>');
        return res.end();        
    }
}).listen(8080); */

/* const EventEmitter = require('events');
const emisorProductos = new EventEmitter();

emisorProductos.on('compra', () => {
    console.log('Se realizo una compra');
});

emisorProductos.emit('compra'); */



/* const EventEmitter = require('events');
const emisorProductos = new EventEmitter();

emisorProductos.on('compra', (total,numProductos) => {
    console.log(`Total compra: ${total}`);
    console.log(`Numero porductos: ${numProductos}`);
});

emisorProductos.emit('compra', 500,5); */

const promesaCumplida = true;

const miPromesa = new Promise((resolve, reject) =>{
    setTimeout(() => {
        if (promesaCumplida) {
            resolve('¡Promesa cumplida!');        
        } else {
            reject('Promesa rechazada...');
        }
               
    }, 5000);
});

miPromesa.then((valor) => {
    console.log(valor);
});

