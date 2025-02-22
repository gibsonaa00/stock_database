#include <stdio.h>
#include <sqlite3.h>

class database{
    public:
    sqlite3 *db;
    int rc;
    database(){
        rc = sqlite3_open("stock.db", &db);
   
        if( rc ) {
            fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
            
            } else {
                fprintf(stdout, "Opened database successfully\n");
                 }
            }

};

int main(void){
    database();
    return 0;
}