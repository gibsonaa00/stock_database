#include <stdio.h>
#include <string>
#include <curl/curl.h>
#include <fstream>
#include <iostream>
#include "settings.hpp"
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main(int argc, char **argv){




    CURL *curl;
    CURLcode res;
    struct curl_slist *headers = nullptr;
    std::string concatString;
    
    //string url = argv[1];

    
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if(curl)  {

        curl_easy_setopt(curl, CURLOPT_URL,argv[1]);

        for (const auto &pair: yfinanceHeaders){
            concatString = pair.first + ":" + pair.second;

            headers = curl_slist_append(headers, concatString.c_str()) ;

        }

       

        // Set the headers
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        // Performs reequest and stroed in res
        res = curl_easy_perform(curl);
        // Error handling
        if (res!= CURLE_OK){
            
        }
        std::string results = std::string(curl_easy_strerror(res));

        //json data = json::parse(results);
        //std::cout << "\n\n:" << data.is_object() << std::endl;
        std::cout  << res << std::endl;

        curl_easy_cleanup(curl);
        curl_global_cleanup();

        
    }
    return 0;
}
