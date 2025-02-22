#include <stdio.h>
#include <string>
#include <curl/curl.h>
#include <fstream>
#include <iostream>
#include "settings.hpp"
#include <nlohmann/json.hpp>
// here is my thoughts use the json to figure the min and max date return it to the terminal and unravel json whilst directly insertting into sqlite
using json = nlohmann::json;
size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main(int argc, char **argv){




    CURL *curl;
    CURLcode res;
    struct curl_slist *headers = nullptr;
    std::string concatString;
    std::string readBuffer;
    
    //string url = argv[1];

    
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if(curl)  {

        curl_easy_setopt(curl, CURLOPT_URL,argv[1]);

        for (const auto &pair: yfinanceHeaders){
            concatString = pair.first + ":" + pair.second;

            headers = curl_slist_append(headers, concatString.c_str()) ;

        }
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

       

        // Set the headers
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        // Performs reequest and stroed in res
        res = curl_easy_perform(curl);
        // Error handling
        if (res!= CURLE_OK){
            
        }

        json data = json::parse(readBuffer);
        std::cout  << readBuffer << std::endl;

        curl_easy_cleanup(curl);
        curl_global_cleanup();

        
    }
    return 0;
}
