#include <iostream>
#include <string>
#include "settings.hpp"
#include <unordered_map>

  std::unordered_map<std::string, std::string> yfinanceHeaders = 
  {
        {"Host", "query1.finance.yahoo.com"} ,
        {"User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0"} ,
        {"Accept","*/*"} ,
        {"Accept-Language", "en-GB,en;q=0.5"} ,
        {"Referer", "https://uk.finance.yahoo.com/quote/TSLA/history/?frequency=1d"} ,
        {"Origin", "https://uk.finance.yahoo.com"} ,
        {"Connection", "keep-alive"} ,
        {"Cookie", "dflow=590; GUC=AQABCAFnm9BnzUIhWAS2&s=AQAAAMGQVB8x&g=Z5qJ1g; EuConsent=CQL_lsAQL_lsAAOACKENBaFgAAAAAAAAACiQAAAAAAAA; A1=d=AQABBMyJmmcCEICrc5e3wfwIJNgs0D4v5zUFEgABCAHQm2fNZ_bPb2UBAiAAAAcIyomaZzsHd6U&S=AQAAAunVRIHwvXvq6SOayBdW_6o; A1S=d=AQABBMyJmmcCEICrc5e3wfwIJNgs0D4v5zUFEgABCAHQm2fNZ_bPb2UBAiAAAAcIyomaZzsHd6U&S=AQAAAunVRIHwvXvq6SOayBdW_6o; A3=d=AQABBMyJmmcCEICrc5e3wfwIJNgs0D4v5zUFEgABCAHQm2fNZ_bPb2UBAiAAAAcIyomaZzsHd6U&S=AQAAAunVRIHwvXvq6SOayBdW_6o; cmp=t=1738181070&j=1&u=1---&v=64; PRF=t%3DTSLA%252B%255EFTSE%252B%255EGSPC"} ,
        {"Sec-Fetch-Dest", "empty"} ,
        {"Sec-Fetch-Mode", "cors"} ,
        {"Sec-Fetch-Site", "same-site"} ,
        {"Priority", "u=0"} ,
        {"Pragma", "no-cache"} ,
        {"Cache-Control", "no-cache"} ,
        {"TE", "trailers" }
      };
