#M_SPOT
import requests
import config  
import websocket 
import numpy
from binance.client import Client  
from binance.enums import *  
import json
import random
import time
import os

client = Client(config.API_KEY, config.API_SECRET)

while 1:
    print('___________________________')
    print('<---Carregando...')
    time.sleep(5)
    
    #Bot_Trade_Iniciado!
    time.sleep(15)
    print('<---Binax-Ativado!--->')
    	
    candles_b = client.get_klines(symbol='CHZUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    
    #preço de abertura, maxima, minima, fechamento
    
    closes_200 = []
    add_closes = closes_200.append(candles_b[-1][4])
    
    add_closes_b = closes_200.append(candles_b[-2][4])
    
    add_closes_c = closes_200.append(candles_b[-3][4])
    
    add_closes_d = closes_200.append(candles_b[-4][4])
    
    add_closes_e = closes_200.append(candles_b[-5][4])
    
    add_closes_f = closes_200.append(candles_b[-6][4])
    
    add_closes_g = closes_200.append(candles_b[-7][4])
    
    add_closes_h = closes_200.append(candles_b[-8][4])
    
    add_closes_i = closes_200.append(candles_b[-9][4])
    
    add_closes_j = closes_200.append(candles_b[-10][4])
    
    add_closes_l = closes_200.append(candles_b[-11][4])
    
    add_closes_n = closes_200.append(candles_b[-12][4])
    
    add_closes_m = closes_200.append(candles_b[-13][4])
    
    add_closes_o = closes_200.append(candles_b[-14][4])
    
    add_closes_p = closes_200.append(candles_b[-15][4])
    
    add_closes_q = closes_200.append(candles_b[-16][4])
    
    add_closes_r = closes_200.append(candles_b[-17][4])
    
    add_closes_s = closes_200.append(candles_b[-18][4])
    
    add_closes_t = closes_200.append(candles_b[-19][4])
    
    add_closes_u = closes_200.append(candles_b[-20][4])
    
    add_closes_v = closes_200.append(candles_b[-21][4])
    
    add_closes_w = closes_200.append(candles_b[-22][4])
    
    add_closes_x = closes_200.append(candles_b[-23][4])
    
    add_closes_y = closes_200.append(candles_b[-24][4])
    
    add_closes_z = closes_200.append(candles_b[-25][4])
    
 
    add_closes_1 = closes_200.append(candles_b[-26][4])
    
    add_closes_2 = closes_200.append(candles_b[-27][4])
    
    add_closes_3 = closes_200.append(candles_b[-28][4])
    
    add_closes_4 = closes_200.append(candles_b[-29][4])
    
    add_closes_5 = closes_200.append(candles_b[-30][4])
    
    add_closes_6 = closes_200.append(candles_b[-31][4])
    
    add_closes_7 = closes_200.append(candles_b[-32][4])
    
    add_closes_8 = closes_200.append(candles_b[-33][4])
    
    add_closes_9 = closes_200.append(candles_b[-34][4])
    
    add_closes_10 = closes_200.append(candles_b[-35][4])
    
    add_closes_11 = closes_200.append(candles_b[-36][4])
    
    add_closes_12 = closes_200.append(candles_b[-37][4])
    
    add_closes_13 = closes_200.append(candles_b[-38][4])
    
    add_closes_14 = closes_200.append(candles_b[-39][4])
    
    add_closes_15 = closes_200.append(candles_b[-40][4])
    
    add_closes_16 = closes_200.append(candles_b[-41][4])
    
    add_closes_17 = closes_200.append(candles_b[-42][4])
    
    add_closes_18 = closes_200.append(candles_b[-43][4])
    
    add_closes_19 = closes_200.append(candles_b[-44][4])
    
    add_closes_20 = closes_200.append(candles_b[-45][4])
    
    add_closes_21 = closes_200.append(candles_b[-46][4])
    
    add_closes_22 = closes_200.append(candles_b[-47][4])
    
    add_closes_23 = closes_200.append(candles_b[-48][4])
    
    add_closes_24 = closes_200.append(candles_b[-49][4])
    
    add_closes_25 = closes_200.append(candles_b[-50][4])
    
    #
    add_closes_26 = closes_200.append(candles_b[-51][4])
    
    add_closes_27 = closes_200.append(candles_b[-52][4])
    
    add_closes_28 = closes_200.append(candles_b[-53][4])
    
    add_closes_29 = closes_200.append(candles_b[-54][4])
    
    add_closes_30 = closes_200.append(candles_b[-55][4])
    
    add_closes_31 = closes_200.append(candles_b[-56][4])
    
    add_closes_32 = closes_200.append(candles_b[-57][4])
    
    add_closes_33 = closes_200.append(candles_b[-58][4])
    
    add_closes_34 = closes_200.append(candles_b[-59][4])
    
    add_closes_35 = closes_200.append(candles_b[-60][4])
    
    add_closes_36 = closes_200.append(candles_b[-61][4])
    
    add_closes_37 = closes_200.append(candles_b[-62][4])
    
    add_closes_38 = closes_200.append(candles_b[-63][4])
    
    add_closes_39 = closes_200.append(candles_b[-64][4])
    
    add_closes_40 = closes_200.append(candles_b[-65][4])
    
    add_closes_41 = closes_200.append(candles_b[-66][4])
    
    add_closes_42 = closes_200.append(candles_b[-67][4])
    
    add_closes_43 = closes_200.append(candles_b[-68][4])
    
    add_closes_44 = closes_200.append(candles_b[-69][4])
    
    add_closes_45 = closes_200.append(candles_b[-70][4])
    
    add_closes_46 = closes_200.append(candles_b[-71][4])
    
    add_closes_47 = closes_200.append(candles_b[-72][4])
    
    add_closes_48 = closes_200.append(candles_b[-73][4])
    
    add_closes_49 = closes_200.append(candles_b[-74][4])
    
    add_closes_50 = closes_200.append(candles_b[-75][4])
    
    #
    add_closes_51 = closes_200.append(candles_b[-76][4])
    
    add_closes_52 = closes_200.append(candles_b[-77][4])
    
    add_closes_53 = closes_200.append(candles_b[-78][4])
    
    add_closes_54 = closes_200.append(candles_b[-79][4])
    
    add_closes_55 = closes_200.append(candles_b[-80][4])
    
    add_closes_56 = closes_200.append(candles_b[-81][4])
    
    add_closes_57 = closes_200.append(candles_b[-82][4])
    
    add_closes_58 = closes_200.append(candles_b[-83][4])
    
    add_closes_59 = closes_200.append(candles_b[-84][4])
    
    add_closes_60 = closes_200.append(candles_b[-85][4])
    
    add_closes_61 = closes_200.append(candles_b[-86][4])
    
    add_closes_62 = closes_200.append(candles_b[-87][4])
    
    add_closes_63 = closes_200.append(candles_b[-88][4])
    
    add_closes_64 = closes_200.append(candles_b[-89][4])
    
    add_closes_65 = closes_200.append(candles_b[-90][4])
    
    add_closes_66 = closes_200.append(candles_b[-91][4])
    
    add_closes_67 = closes_200.append(candles_b[-92][4])
    
    add_closes_68 = closes_200.append(candles_b[-93][4])
    
    add_closes_69 = closes_200.append(candles_b[-94][4])
    
    add_closes_70 = closes_200.append(candles_b[-95][4])
    
    add_closes_71 = closes_200.append(candles_b[-96][4])
    
    add_closes_72 = closes_200.append(candles_b[-97][4])
    
    add_closes_73 = closes_200.append(candles_b[-98][4])
    
    add_closes_74 = closes_200.append(candles_b[-99][4])
    
    add_closes_75 = closes_200.append(candles_b[-100][4])
    
    #
    add_closes_76 = closes_200.append(candles_b[-101][4])
    
    add_closes_77 = closes_200.append(candles_b[-102][4])
    
    add_closes_78 = closes_200.append(candles_b[-103][4])
    
    add_closes_79 = closes_200.append(candles_b[-104][4])
    
    add_closes_80 = closes_200.append(candles_b[-105][4])
    
    add_closes_81 = closes_200.append(candles_b[-106][4])
    
    add_closes_82 = closes_200.append(candles_b[-107][4])
    
    add_closes_83 = closes_200.append(candles_b[-108][4])
    
    add_closes_84 = closes_200.append(candles_b[-109][4])
    
    add_closes_85 = closes_200.append(candles_b[-110][4])
    
    add_closes_86 = closes_200.append(candles_b[-111][4])
    
    add_closes_87 = closes_200.append(candles_b[-112][4])
    
    add_closes_88 = closes_200.append(candles_b[-113][4])
    
    add_closes_89 = closes_200.append(candles_b[-114][4])
    
    add_closes_90 = closes_200.append(candles_b[-115][4])
    
    add_closes_91 = closes_200.append(candles_b[-116][4])
    
    add_closes_92 = closes_200.append(candles_b[-117][4])
    
    add_closes_93 = closes_200.append(candles_b[-118][4])
    
    add_closes_94 = closes_200.append(candles_b[-119][4])
    
    add_closes_95 = closes_200.append(candles_b[-120][4])
    
    add_closes_96 = closes_200.append(candles_b[-121][4])
    
    add_closes_97 = closes_200.append(candles_b[-122][4])
    
    add_closes_98 = closes_200.append(candles_b[-123][4])
    
    add_closes_99 = closes_200.append(candles_b[-124][4])
    
    add_closes_100 = closes_200.append(candles_b[-125][4])
    
    #
    add_closes_101 = closes_200.append(candles_b[-126][4])
    
    add_closes_102 = closes_200.append(candles_b[-127][4])
    
    add_closes_103 = closes_200.append(candles_b[-128][4])
    
    add_closes_104 = closes_200.append(candles_b[-129][4])
    
    add_closes_105 = closes_200.append(candles_b[-130][4])
    
    add_closes_106 = closes_200.append(candles_b[-131][4])
    
    add_closes_107 = closes_200.append(candles_b[-132][4])
    
    add_closes_108 = closes_200.append(candles_b[-133][4])
    
    add_closes_109 = closes_200.append(candles_b[-134][4])
    
    add_closes_110 = closes_200.append(candles_b[-135][4])
    
    add_closes_111 = closes_200.append(candles_b[-136][4])
    
    add_closes_112 = closes_200.append(candles_b[-137][4])
    
    add_closes_113 = closes_200.append(candles_b[-138][4])
    
    add_closes_114 = closes_200.append(candles_b[-139][4])
    
    add_closes_115 = closes_200.append(candles_b[-140][4])
    
    add_closes_116 = closes_200.append(candles_b[-141][4])
    
    add_closes_117 = closes_200.append(candles_b[-142][4])
    
    add_closes_118 = closes_200.append(candles_b[-143][4])
    
    add_closes_119 = closes_200.append(candles_b[-144][4])
    
    add_closes_120 = closes_200.append(candles_b[-145][4])
    
    add_closes_121 = closes_200.append(candles_b[-146][4])
    
    add_closes_122 = closes_200.append(candles_b[-147][4])
    
    add_closes_123 = closes_200.append(candles_b[-148][4])
    
    add_closes_124 = closes_200.append(candles_b[-149][4])
    
    add_closes_125 = closes_200.append(candles_b[-150][4])
    
    #
    add_closes_126 = closes_200.append(candles_b[-151][4])
    
    add_closes_127 = closes_200.append(candles_b[-152][4])
    
    add_closes_128 = closes_200.append(candles_b[-153][4])
    
    add_closes_129 = closes_200.append(candles_b[-154][4])
    
    add_closes_130 = closes_200.append(candles_b[-155][4])
    
    add_closes_131 = closes_200.append(candles_b[-156][4])
    
    add_closes_132 = closes_200.append(candles_b[-157][4])
    
    add_closes_133 = closes_200.append(candles_b[-158][4])
    
    add_closes_134 = closes_200.append(candles_b[-159][4])
    
    add_closes_135 = closes_200.append(candles_b[-160][4])
    
    add_closes_136 = closes_200.append(candles_b[-161][4])
    
    add_closes_137 = closes_200.append(candles_b[-162][4])
    
    add_closes_138 = closes_200.append(candles_b[-163][4])
    
    add_closes_139 = closes_200.append(candles_b[-164][4])
    
    add_closes_140 = closes_200.append(candles_b[-165][4])
    
    add_closes_141 = closes_200.append(candles_b[-166][4])
    
    add_closes_142 = closes_200.append(candles_b[-167][4])
    
    add_closes_143 = closes_200.append(candles_b[-168][4])
    #168p
    
   
    np = closes_200
    #print('Ultimos 168 fechamentos',np)
    float_np = list(numpy.array(np, dtype='float'))
    lst_np = numpy.array(float_np)
    soma = sum(lst_np)
    #print('soma',soma)
    result_sm = soma/168
    media2_rd = round(result_sm, 4)
    print('___________________________')
    print('<---MÉDIA 168p:',media2_rd)
    #---------#
    
    resposta = requests.get('https://api.taapi.io/rsi?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM3NTE4YjhmYzVhOGFkZmVjMWVhZWM4IiwiaWF0IjoxNjY4NjE4NDI0LCJleHAiOjMzMTczMDgyNDI0fQ.MuFuAO1q4s-UpYB_8CFGcivBglViDVveJzkTjJCei1c&exchange=binance&symbol=BTC/USDT&interval=15m')

    dados = resposta.json()

    ac_dir = (dados['value'])
    #RSI
    rsi_10 = round(ac_dir, 2)

    print('<---RSI-BTC>: ', rsi_10)
        
    #DEFINIR A ESTRATEGIA DE BUY/SELL
    
    RSI_BULL = 70.0
    RSI_N = 60.0
    RSI_BEAR = 30.0
    
    qt_usdt = 0.001
    qt_usdt_rd = round(qt_usdt, 2)
    #print('saldo::',qt_usdt_rd)
    
    STOP_GAIN = 0.10 #+0.10%xALA
    
    STOP_LOSS = 0.00  #-0.00%xALA
    
    trades = client.get_my_trades(symbol='CHZUSDT')
    price_buy = (trades[-1])
    price_buy_b = float(price_buy['price'])
    sprice = price_buy_b
    #print('PRICE_F:::', sprice)
    #print('trades:::', trades)
    rd_a = round (sprice, 4)  
    sm = sprice * 0.04
    sm_2 = sm + sprice  
    rd = round (sm_2, 4)  
    price_sell = rd 
    stop_loss_g = sprice * 0.02
    stop_loss_gb = sprice - stop_loss_g
    stop_loss_gbr = round(stop_loss_gb, 4)
    #COMPRAR
    print('<---LONG_STOP_GAIN:',price_sell)
    print('<---LONG_STOP_LOSS:',stop_loss_gbr)
    #RECOMPAR -1%
    rp_buy = rd_a * 0.01
    rp_buy_b = round(rd_a - rp_buy, 4)
    
    print('<---Recomprar:', rp_buy_b)
    
    price_btc = client.get_symbol_ticker(symbol='CHZUSDT')
    price_at = float(price_btc['price'])
    print('<---PREÇO ATUAL:', price_at)
    
    #saldo usdt
    saldo_usdt = client.get_asset_balance(asset='USDT')
    usdtsaldo = float(saldo_usdt["free"])
    saldo_usdt_b = round(usdtsaldo, 2)
    sl_d = saldo_usdt_b - 0.01
    usdt_rd = round(sl_d, 2)
    print('<---saldo usdt:', usdt_rd)
    qt_btc = sl_d / price_at
    qt_btc_rd = round(qt_btc, 0)
    print('<---QT-CHZ:', qt_btc_rd)
    
    #saldo btc
    saldo_btc = client.get_asset_balance(asset='CHZ')
    btcsaldo = float(saldo_btc["free"])
    saldo_btc_b = round(btcsaldo, 0)
    saldo_btc_c = saldo_btc_b - 1.0
    print('<---saldo chz:',saldo_btc_c)
    
    sd_a = 50.0
    saldo_usdt = 10.50
    
    #STOP-GAIN	
    if (saldo_btc_b >= sd_a):
        order_sell = client.order_limit_sell(
        symbol='CHZUSDT',
        quantity=saldo_btc_c,
        price=price_sell)
        print('<---ORDEM DE VENDA CRIADA !!!')
        
    else:
    	print('<---SALDO INSUFICIENTE!')
    	
   #definir_stop_loss   
    if (price_at <= stop_loss_gbr):
        orderst = client.get_open_orders(symbol='CHZUSDT')
        select_ul = orderst[-1]
        prid = (select_ul['orderId'])
        result = client.cancel_order(
        symbol='CHZUSDT',
        orderId=prid)
        order = client.order_market_sell(
        symbol='CHZUSDT',
        quantity=saldo_btc_c)
        print('<---STOP-ATIVADO !!!')
        
    else:
      	print('<---PS-GAIN--->')
    	 
    #versão_compra
    if (price_at > media2_rd) and (rsi_10 <= RSI_N) and (usdt_rd >= saldo_usdt) and (price_at < rd_a):
    	print('<---BUY !!! SETUP 1')
    	order = client.order_market_buy(
        symbol='CHZUSDT',
        quantity=qt_btc_rd)
        
    else:
    	print('<---SETUP 1 NÃO CONFIRMADO!')
        
    if (price_at < rd_a) and (rsi_10 <= RSI_BEAR)and (usdt_rd >= saldo_usdt):
    	print('<---BUY !!! SETUP 2')
    	order = client.order_market_buy(
    	symbol='CHZUSDT',
    	quantity=qt_btc_rd)
    	
    else:
    	print('<---SETUP 2 NÃO CONFIRMADO!')
    	
    #NovaRecompra   
    if (usdt_rd >= saldo_usdt) and (price_at < rd_a):
        order_by = client.order_limit_buy(
        symbol='CHZUSDT',
        quantity=qt_btc_rd,
        price=rp_buy_b)
        print('<---Nova Recompra criada!')
        
    else:
      	print('<---SALDO USDT INSUFICIENTE!')


