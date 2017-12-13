#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Kyle Dornblaser"
__version__ = "0.1.0"
__license__ = "MIT"

#from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html>
<html lang="en-US" dir="ltr">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="A free collaborative calendar for all upcoming crypto events. Evidence-based & Community-driven.">
    <meta name="keywords" content="cryptocurrency, coinmarketcap, coinscalendar, coins, crypto, currency, calendar, events, collaborative, bitcoin">
    <title>Cryptocurrency Calendar</title>
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-icon-57x57.png"/>
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-icon-60x60.png"/>
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/manifest.json">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="/ms-icon-144x144.png">
    <meta name="theme-color" content="#ffffff">

    <link href="/lib/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed:400,700" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Volkhov:400i" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800" rel="stylesheet">
        <link rel="stylesheet" href="/css/2680ec3.css" type="text/css"/>
        <link href="/css/style.css" rel="stylesheet">
    <meta property="og:locale" content="en_US"/>
    <meta property="og:site_name" content="Coinmarketcal"/>
    <meta property="og:title" content="Cryptocurrency Calendar"/>
    <meta property="og:url" content="http://coinmarketcal.com"/>
    <meta property="og:type" content="website"/>
    <meta property="og:image" content="http://coinmarketcal.com/images/banner.jpg"/>
    <meta property="og:description" content="A free collaborative calendar for all upcoming crypto events. Evidence-based & Community-driven."/>
    <meta itemprop="name" content="Events"/>
    <meta itemprop="description" content="A free collaborative calendar for all upcoming crypto events. Evidence-based & Community-driven."/>
    <meta itemprop="image" content="http://coinmarketcal.com/images/banner.jpg"/>
    <meta name="twitter:title" content="Cryptocurrency Calendar"/>
    <meta name="twitter:url" content="http://coinmarketcal.com"/>
    <meta name="twitter:description" content="A free collaborative calendar for all upcoming crypto events. Evidence-based & Community-driven."/>
    <meta name="twitter:image" content="http://coinmarketcal.com/images/banner.jpg"/>
    <meta name="twitter:site" content="@coinmarketcal"/>

</head>

<body data-spy="scroll" data-target=".onpage-navigation" data-offset="60">
<script type="text/javascript">
    (function () {
        var bsa = document.createElement('script');
        bsa.type = 'text/javascript';
        bsa.async = true;
        bsa.src = '//s3.buysellads.com/ac/bsa.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(bsa);
    })();
</script>
<main>
    <div class="modal fade" id="alertModal" tabindex="-1" role="dialog" aria-labelledby="alertModal">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="exampleModalLabel">Create your alert</h4>
            </div>
            <form name="new_alert_form" method="post" class="form" role="form" id="form_alert_add">
            <div class="modal-body">

                <div class="form-group">
                    <label>I want be notified when an event for:</label>
                    <div class="error"></div>
                    <select id="new_alert_form_coin" name="new_alert_form[coin][]" required="required" class="selectpicker form-control" data-live-search="true" title="Select coin(s)" tabindex="1" id="recipient-coin" multiple="multiple"><option value="Bitcoin (BTC)">Bitcoin (BTC)</option><option value="Ethereum (ETH)">Ethereum (ETH)</option><option value="Bitcoin Cash (BCH)">Bitcoin Cash (BCH)</option><option value="IOTA (MIOTA)">IOTA (MIOTA)</option><option value="Ripple (XRP)">Ripple (XRP)</option><option value="Litecoin (LTC)">Litecoin (LTC)</option><option value="Dash (DASH)">Dash (DASH)</option><option value="Bitcoin Gold (BTG)">Bitcoin Gold (BTG)</option><option value="Monero (XMR)">Monero (XMR)</option><option value="NEM (XEM)">NEM (XEM)</option><option value="Cardano (ADA)">Cardano (ADA)</option><option value="Ethereum Classic (ETC)">Ethereum Classic (ETC)</option><option value="Stellar Lumens (XLM)">Stellar Lumens (XLM)</option><option value="NEO (NEO)">NEO (NEO)</option><option value="EOS (EOS)">EOS (EOS)</option><option value="BitConnect (BCC)">BitConnect (BCC)</option><option value="Populous (PPT)">Populous (PPT)</option><option value="Waves (WAVES)">Waves (WAVES)</option><option value="Lisk (LSK)">Lisk (LSK)</option><option value="Stratis (STRAT)">Stratis (STRAT)</option><option value="Qtum (QTUM)">Qtum (QTUM)</option><option value="Zcash (ZEC)">Zcash (ZEC)</option><option value="OmiseGO (OMG)">OmiseGO (OMG)</option><option value="Tether (USDT)">Tether (USDT)</option><option value="MonaCoin (MONA)">MonaCoin (MONA)</option><option value="Hshare (HSR)">Hshare (HSR)</option><option value="Nxt (NXT)">Nxt (NXT)</option><option value="Ardor (ARDR)">Ardor (ARDR)</option><option value="Bytecoin (BCN)">Bytecoin (BCN)</option><option value="BitShares (BTS)">BitShares (BTS)</option><option value="Steem (STEEM)">Steem (STEEM)</option><option value="SALT (SALT)">SALT (SALT)</option><option value="Einsteinium (EMC2)">Einsteinium (EMC2)</option><option value="Decred (DCR)">Decred (DCR)</option><option value="Ark (ARK)">Ark (ARK)</option><option value="Vertcoin (VTC)">Vertcoin (VTC)</option><option value="Veritaseum (VERI)">Veritaseum (VERI)</option><option value="Augur (REP)">Augur (REP)</option><option value="Komodo (KMD)">Komodo (KMD)</option><option value="TRON (TRX)">TRON (TRX)</option><option value="Dogecoin (DOGE)">Dogecoin (DOGE)</option><option value="Siacoin (SC)">Siacoin (SC)</option><option value="Binance Coin (BNB)">Binance Coin (BNB)</option><option value="Golem (GNT)">Golem (GNT)</option><option value="QASH (QASH)">QASH (QASH)</option><option value="PIVX (PIVX)">PIVX (PIVX)</option><option value="Santiment Network Token (SAN)">Santiment Network Token (SAN)</option><option value="TenX (PAY)">TenX (PAY)</option><option value="MaidSafeCoin (MAID)">MaidSafeCoin (MAID)</option><option value="Status (SNT)">Status (SNT)</option><option value="DigixDAO (DGD)">DigixDAO (DGD)</option><option value="Byteball Bytes (GBYTE)">Byteball Bytes (GBYTE)</option><option value="Exchange Union (XUC)">Exchange Union (XUC)</option><option value="Cryptonex (CNX)">Cryptonex (CNX)</option><option value="Basic Attention Token (BAT)">Basic Attention Token (BAT)</option><option value="Power Ledger (POWR)">Power Ledger (POWR)</option><option value="Walton (WTC)">Walton (WTC)</option><option value="BitcoinDark (BTCD)">BitcoinDark (BTCD)</option><option value="Factom (FCT)">Factom (FCT)</option><option value="Syscoin (SYS)">Syscoin (SYS)</option><option value="Decentraland (MANA)">Decentraland (MANA)</option><option value="Kyber Network (KNC)">Kyber Network (KNC)</option><option value="Bytom (BTM)">Bytom (BTM)</option><option value="Pura (PURA)">Pura (PURA)</option><option value="Monaco (MCO)">Monaco (MCO)</option><option value="Raiden Network Token (RDN)">Raiden Network Token (RDN)</option><option value="Gas (GAS)">Gas (GAS)</option><option value="ZCoin (XZC)">ZCoin (XZC)</option><option value="Aeternity (AE)">Aeternity (AE)</option><option value="Iconomi (ICN)">Iconomi (ICN)</option><option value="VeChain (VEN)">VeChain (VEN)</option><option value="GameCredits (GAME)">GameCredits (GAME)</option><option value="DigiByte (DGB)">DigiByte (DGB)</option><option value="RaiBlocks (XRB)">RaiBlocks (XRB)</option><option value="FunFair (FUN)">FunFair (FUN)</option><option value="Verge (XVG)">Verge (XVG)</option><option value="Gnosis (GNO)">Gnosis (GNO)</option><option value="Nexus (NXS)">Nexus (NXS)</option><option value="0x (ZRX)">0x (ZRX)</option><option value="Request Network (REQ)">Request Network (REQ)</option><option value="Blocknet (BLOCK)">Blocknet (BLOCK)</option><option value="Bancor (BNT)">Bancor (BNT)</option><option value="Dragonchain (DRGN)">Dragonchain (DRGN)</option><option value="Metal (MTL)">Metal (MTL)</option><option value="Civic (CVC)">Civic (CVC)</option><option value="Skycoin (SKY)">Skycoin (SKY)</option><option value="Ethos (ETHOS)">Ethos (ETHOS)</option><option value="ChainLink (LINK)">ChainLink (LINK)</option><option value="Edgeless (EDG)">Edgeless (EDG)</option><option value="Aion (AION)">Aion (AION)</option><option value="NAV Coin (NAV)">NAV Coin (NAV)</option><option value="Storj (STORJ)">Storj (STORJ)</option><option value="GXShares (GXS)">GXShares (GXS)</option><option value="Streamr DATAcoin (DATA)">Streamr DATAcoin (DATA)</option><option value="Metaverse ETP (ETP)">Metaverse ETP (ETP)</option><option value="ATMChain (ATM)">ATMChain (ATM)</option><option value="RChain (RHOC)">RChain (RHOC)</option><option value="Jinn (JINN)">Jinn (JINN)</option><option value="MinexCoin (MNX)">MinexCoin (MNX)</option><option value="Achain (ACT)">Achain (ACT)</option><option value="Substratum (SUB)">Substratum (SUB)</option><option value="Revain (R)">Revain (R)</option><option value="Peercoin (PPC)">Peercoin (PPC)</option><option value="Pepe Cash (PEPECASH)">Pepe Cash (PEPECASH)</option><option value="Lykke (LKK)">Lykke (LKK)</option><option value="Groestlcoin (GRS)">Groestlcoin (GRS)</option><option value="BitBay (BAY)">BitBay (BAY)</option><option value="ZenCash (ZEN)">ZenCash (ZEN)</option><option value="AdEx (ADX)">AdEx (ADX)</option><option value="SingularDTV (SNGLS)">SingularDTV (SNGLS)</option><option value="Ubiq (UBQ)">Ubiq (UBQ)</option><option value="MobileGo (MGO)">MobileGo (MGO)</option><option value="Feathercoin (FTC)">Feathercoin (FTC)</option><option value="Quantstamp (QSP)">Quantstamp (QSP)</option><option value="PotCoin (POT)">PotCoin (POT)</option><option value="Particl (PART)">Particl (PART)</option><option value="Aragon (ANT)">Aragon (ANT)</option><option value="YOYOW (YOYOW)">YOYOW (YOYOW)</option><option value="FairCoin (FAIR)">FairCoin (FAIR)</option><option value="Loopring (LRC)">Loopring (LRC)</option><option value="Asch (XAS)">Asch (XAS)</option><option value="Cobinhood (COB)">Cobinhood (COB)</option><option value="Quantum Resistant Ledger (QRL)">Quantum Resistant Ledger (QRL)</option><option value="Ripio Credit Network (RCN)">Ripio Credit Network (RCN)</option><option value="PayPie (PPP)">PayPie (PPP)</option><option value="Counterparty (XCP)">Counterparty (XCP)</option><option value="Ink (INK)">Ink (INK)</option><option value="Open Trading Network (OTN)">Open Trading Network (OTN)</option><option value="Aeon (AEON)">Aeon (AEON)</option><option value="Viacoin (VIA)">Viacoin (VIA)</option><option value="Agoras Tokens (AGRS)">Agoras Tokens (AGRS)</option><option value="Mercury (MER)">Mercury (MER)</option><option value="FedoraCoin (TIPS)">FedoraCoin (TIPS)</option><option value="Eidoo (EDO)">Eidoo (EDO)</option><option value="SONM (SNM)">SONM (SNM)</option><option value="Wings (WINGS)">Wings (WINGS)</option><option value="ReddCoin (RDD)">ReddCoin (RDD)</option><option value="Kin (KIN)">Kin (KIN)</option><option value="Melon (MLN)">Melon (MLN)</option><option value="Neblio (NEBL)">Neblio (NEBL)</option><option value="KuCoin Shares (KCS)">KuCoin Shares (KCS)</option><option value="WeTrust (TRST)">WeTrust (TRST)</option><option value="Blocktix (TIX)">Blocktix (TIX)</option><option value="Russian Miner Coin (RMC)">Russian Miner Coin (RMC)</option><option value="Rise (RISE)">Rise (RISE)</option><option value="iExec RLC (RLC)">iExec RLC (RLC)</option><option value="Diamond (DMD)">Diamond (DMD)</option><option value="Emercoin (EMC)">Emercoin (EMC)</option><option value="Voxels (VOX)">Voxels (VOX)</option><option value="Namecoin (NMC)">Namecoin (NMC)</option><option value="Enigma (ENG)">Enigma (ENG)</option><option value="Safe Exchange Coin (SAFEX)">Safe Exchange Coin (SAFEX)</option><option value="BLOCKv (VEE)">BLOCKv (VEE)</option><option value="Wagerr (WGR)">Wagerr (WGR)</option><option value="Zeusshield (ZSC)">Zeusshield (ZSC)</option><option value="CloakCoin (CLOAK)">CloakCoin (CLOAK)</option><option value="SIBCoin (SIB)">SIBCoin (SIB)</option><option value="TaaS (TAAS)">TaaS (TAAS)</option><option value="WhiteCoin (XWC)">WhiteCoin (XWC)</option><option value="Bitcore (BTX)">Bitcore (BTX)</option><option value="AirSwap (AST)">AirSwap (AST)</option><option value="CoinDash (CDT)">CoinDash (CDT)</option><option value="SmartCash (SMART)">SmartCash (SMART)</option><option value="Pillar (PLR)">Pillar (PLR)</option><option value="NoLimitCoin (NLC2)">NoLimitCoin (NLC2)</option><option value="Cofound.it (CFI)">Cofound.it (CFI)</option><option value="Tierion (TNT)">Tierion (TNT)</option><option value="I/O Coin (IOC)">I/O Coin (IOC)</option><option value="Enjin Coin (ENJ)">Enjin Coin (ENJ)</option><option value="DECENT (DCT)">DECENT (DCT)</option><option value="Gulden (NLG)">Gulden (NLG)</option><option value="Crown (CRW)">Crown (CRW)</option><option value="bitqy (BQ)">bitqy (BQ)</option><option value="Modum (MOD)">Modum (MOD)</option><option value="OKCash (OK)">OKCash (OK)</option><option value="Time New Bank (TNB)">Time New Bank (TNB)</option><option value="Presearch (PRE)">Presearch (PRE)</option><option value="SaluS (SLS)">SaluS (SLS)</option><option value="Numeraire (NMR)">Numeraire (NMR)</option><option value="Paypex (PAYX)">Paypex (PAYX)</option><option value="Cindicator (CND)">Cindicator (CND)</option><option value="FirstBlood (1ST)">FirstBlood (1ST)</option><option value="Ambrosus (AMB)">Ambrosus (AMB)</option><option value="Bitzeny (ZNY)">Bitzeny (ZNY)</option><option value="Centra (CTR)">Centra (CTR)</option><option value="LBRY Credits (LBC)">LBRY Credits (LBC)</option><option value="Delphy (DPY)">Delphy (DPY)</option><option value="Steem Dollars (SBD)">Steem Dollars (SBD)</option><option value="XTRABYTES (XBY)">XTRABYTES (XBY)</option><option value="BitDice (CSNO)">BitDice (CSNO)</option><option value="GridCoin (GRC)">GridCoin (GRC)</option><option value="Burst (BURST)">Burst (BURST)</option><option value="ION (ION)">ION (ION)</option><option value="Moeda Loyalty Points (MDA)">Moeda Loyalty Points (MDA)</option><option value="district0x (DNT)">district0x (DNT)</option><option value="Grid+ (GRID)">Grid+ (GRID)</option><option value="Triggers (TRIG)">Triggers (TRIG)</option><option value="Dentacoin (DCN)">Dentacoin (DCN)</option><option value="Matchpool (GUP)">Matchpool (GUP)</option><option value="Global Currency Reserve (GCR)">Global Currency Reserve (GCR)</option><option value="Waves Community Token (WCT)">Waves Community Token (WCT)</option><option value="Shift (SHIFT)">Shift (SHIFT)</option><option value="Golos (GOLOS)">Golos (GOLOS)</option><option value="Unikoin Gold (UKG)">Unikoin Gold (UKG)</option><option value="BlackCoin (BLK)">BlackCoin (BLK)</option><option value="ClearPoll (POLL)">ClearPoll (POLL)</option><option value="Boolberry (BBR)">Boolberry (BBR)</option><option value="Xaurum (XAUR)">Xaurum (XAUR)</option><option value="Dimecoin (DIME)">Dimecoin (DIME)</option><option value="Polybius (PLBT)">Polybius (PLBT)</option><option value="TransferCoin (TX)">TransferCoin (TX)</option><option value="LEOcoin (LEO)">LEOcoin (LEO)</option><option value="ICOS (ICOS)">ICOS (ICOS)</option><option value="Dent (DENT)">Dent (DENT)</option><option value="Aventus (AVT)">Aventus (AVT)</option><option value="HempCoin (THC)">HempCoin (THC)</option><option value="Omni (OMNI)">Omni (OMNI)</option><option value="Humaniq (HMQ)">Humaniq (HMQ)</option><option value="EncrypGen (DNA)">EncrypGen (DNA)</option><option value="SpankChain (SPANK)">SpankChain (SPANK)</option><option value="XPlay (XPA)">XPlay (XPA)</option><option value="MonetaryUnit (MUE)">MonetaryUnit (MUE)</option><option value="Elastic (XEL)">Elastic (XEL)</option><option value="ETHLend (LEND)">ETHLend (LEND)</option><option value="Red Pulse (RPX)">Red Pulse (RPX)</option><option value="Etherparty (FUEL)">Etherparty (FUEL)</option><option value="Synereo (AMP)">Synereo (AMP)</option><option value="iXledger (IXT)">iXledger (IXT)</option><option value="Po.et (POE)">Po.et (POE)</option><option value="Rubycoin (RBY)">Rubycoin (RBY)</option><option value="DigitalNote (XDN)">DigitalNote (XDN)</option><option value="ATBCoin (ATB)">ATBCoin (ATB)</option><option value="TokenCard (TKN)">TokenCard (TKN)</option><option value="Stox (STX)">Stox (STX)</option><option value="Genesis Vision (GVT)">Genesis Vision (GVT)</option><option value="Paragon (PRG)">Paragon (PRG)</option><option value="Viberate (VIB)">Viberate (VIB)</option><option value="Clams (CLAM)">Clams (CLAM)</option><option value="Everex (EVX)">Everex (EVX)</option><option value="Rialto (XRL)">Rialto (XRL)</option><option value="Agrello (DLT)">Agrello (DLT)</option><option value="SolarCoin (SLR)">SolarCoin (SLR)</option><option value="Hive (HVN)">Hive (HVN)</option><option value="SunContract (SNC)">SunContract (SNC)</option><option value="OBITS (OBITS)">OBITS (OBITS)</option><option value="Monetha (MTH)">Monetha (MTH)</option><option value="Etheroll (DICE)">Etheroll (DICE)</option><option value="BitSend (BSD)">BitSend (BSD)</option><option value="The ChampCoin (TCC)">The ChampCoin (TCC)</option><option value="CasinoCoin (CSC)">CasinoCoin (CSC)</option><option value="Gambit (GAM)">Gambit (GAM)</option><option value="Sphere (SPHR)">Sphere (SPHR)</option><option value="ALIS (ALIS)">ALIS (ALIS)</option><option value="BridgeCoin (BCO)">BridgeCoin (BCO)</option><option value="Radium (RADS)">Radium (RADS)</option><option value="Nimiq (NET)">Nimiq (NET)</option><option value="Databits (DTB)">Databits (DTB)</option><option value="Target Coin (TGT)">Target Coin (TGT)</option><option value="NeosCoin (NEOS)">NeosCoin (NEOS)</option><option value="Pascal Coin (PASC)">Pascal Coin (PASC)</option><option value="Unobtanium (UNO)">Unobtanium (UNO)</option><option value="Oxycoin (OXY)">Oxycoin (OXY)</option><option value="bitCNY (BITCNY)">bitCNY (BITCNY)</option><option value="NVO (NVST)">NVO (NVST)</option><option value="Peerplays (PPY)">Peerplays (PPY)</option><option value="OracleChain (OCT)">OracleChain (OCT)</option><option value="adToken (ADT)">adToken (ADT)</option><option value="Soarcoin (SOAR)">Soarcoin (SOAR)</option><option value="VeriCoin (VRC)">VeriCoin (VRC)</option><option value="BCAP (BCAP)">BCAP (BCAP)</option><option value="Expanse (EXP)">Expanse (EXP)</option><option value="Mothership (MSP)">Mothership (MSP)</option><option value="Bitdeal (BDL)">Bitdeal (BDL)</option><option value="Centurion (CNT)">Centurion (CNT)</option><option value="Vcash (XVC)">Vcash (XVC)</option><option value="Xenon (XNN)">Xenon (XNN)</option><option value="FoldingCoin (FLDC)">FoldingCoin (FLDC)</option><option value="KickCoin (KICK)">KickCoin (KICK)</option><option value="Primas (PST)">Primas (PST)</option><option value="DeepOnion (ONION)">DeepOnion (ONION)</option><option value="Tao (XTO)">Tao (XTO)</option><option value="FlorinCoin (FLO)">FlorinCoin (FLO)</option><option value="NuShares (NSR)">NuShares (NSR)</option><option value="DomRaider (DRT)">DomRaider (DRT)</option><option value="Mysterium (MYST)">Mysterium (MYST)</option><option value="InvestFeed (IFT)">InvestFeed (IFT)</option><option value="MCAP (MCAP)">MCAP (MCAP)</option><option value="Rivetz (RVT)">Rivetz (RVT)</option><option value="Energycoin (ENRG)">Energycoin (ENRG)</option><option value="ToaCoin (TOA)">ToaCoin (TOA)</option><option value="LoMoCoin (LMC)">LoMoCoin (LMC)</option><option value="Blackmoon Crypto (BMC)">Blackmoon Crypto (BMC)</option><option value="Chronobank (TIME)">Chronobank (TIME)</option><option value="Lunyr (LUN)">Lunyr (LUN)</option><option value="HEAT (HEAT)">HEAT (HEAT)</option><option value="Swarm City (SWT)">Swarm City (SWT)</option><option value="Patientory (PTOY)">Patientory (PTOY)</option><option value="Nexium (NXC)">Nexium (NXC)</option><option value="Obsidian (ODN)">Obsidian (ODN)</option><option value="BitBean (BITB)">BitBean (BITB)</option><option value="Bitcloud (BTDX)">Bitcloud (BTDX)</option><option value="Change (CAG)">Change (CAG)</option><option value="Bitmark (BTM)">Bitmark (BTM)</option><option value="Masternodecoin (MTNC)">Masternodecoin (MTNC)</option><option value="Novacoin (NVC)">Novacoin (NVC)</option><option value="Curecoin (CURE)">Curecoin (CURE)</option><option value="Maecenas (ART)">Maecenas (ART)</option><option value="Decision Token (HST)">Decision Token (HST)</option><option value="BlockCAT (CAT)">BlockCAT (CAT)</option><option value="Incent (INCNT)">Incent (INCNT)</option><option value="Sequence (SEQ)">Sequence (SEQ)</option><option value="eBitcoin (EBTC)">eBitcoin (EBTC)</option><option value="DubaiCoin (DBIX)">DubaiCoin (DBIX)</option><option value="AirToken (AIR)">AirToken (AIR)</option><option value="bitUSD (BITUSD)">bitUSD (BITUSD)</option><option value="Credo (CREDO)">Credo (CREDO)</option><option value="PRIZM (PZM)">PRIZM (PZM)</option><option value="EncryptoTel [WAVES] (ETT)">EncryptoTel [WAVES] (ETT)</option><option value="Quantum (QAU)">Quantum (QAU)</option><option value="DecentBet (DBET)">DecentBet (DBET)</option><option value="PinkCoin (PINK)">PinkCoin (PINK)</option><option value="OAX (OAX)">OAX (OAX)</option><option value="Auroracoin (AUR)">Auroracoin (AUR)</option><option value="Mooncoin (MOON)">Mooncoin (MOON)</option><option value="BLUE (BLUE)">BLUE (BLUE)</option><option value="COSS (COSS)">COSS (COSS)</option><option value="Onix (ONX)">Onix (ONX)</option><option value="Bitcrystals (BCY)">Bitcrystals (BCY)</option><option value="PoSW Coin (POSW)">PoSW Coin (POSW)</option><option value="Bitcoin Plus (XBC)">Bitcoin Plus (XBC)</option><option value="Dynamic (DYN)">Dynamic (DYN)</option><option value="Pluton (PLU)">Pluton (PLU)</option><option value="Musicoin (MUSIC)">Musicoin (MUSIC)</option><option value="Pesetacoin (PTC)">Pesetacoin (PTC)</option><option value="DAO.Casino (BET)">DAO.Casino (BET)</option><option value="Stealthcoin (XST)">Stealthcoin (XST)</option><option value="Ethereum Movie Venture (EMV)">Ethereum Movie Venture (EMV)</option><option value="E-Dinar Coin (EDR)">E-Dinar Coin (EDR)</option><option value="Internet of People (IOP)">Internet of People (IOP)</option><option value="Primalbase Token (PBT)">Primalbase Token (PBT)</option><option value="BlockMason Credit Protocol (BCPT)">BlockMason Credit Protocol (BCPT)</option><option value="BlueCoin (BLU)">BlueCoin (BLU)</option><option value="EarthCoin (EAC)">EarthCoin (EAC)</option><option value="ECC (ECC)">ECC (ECC)</option><option value="Syndicate (SYNX)">Syndicate (SYNX)</option><option value="Myriad (XMY)">Myriad (XMY)</option><option value="VIBE (VIBE)">VIBE (VIBE)</option><option value="Sexcoin (SXC)">Sexcoin (SXC)</option><option value="CVCoin (CVCOIN)">CVCoin (CVCOIN)</option><option value="Neutron (NTRN)">Neutron (NTRN)</option><option value="CryptoPing (PING)">CryptoPing (PING)</option><option value="Dovu (DOVU)">Dovu (DOVU)</option><option value="Mintcoin (MINT)">Mintcoin (MINT)</option><option value="Kore (KORE)">Kore (KORE)</option><option value="Lampix (PIX)">Lampix (PIX)</option><option value="LAToken (LA)">LAToken (LA)</option><option value="NewYorkCoin (NYC)">NewYorkCoin (NYC)</option><option value="Bankcoin (B@)">Bankcoin (B@)</option><option value="ZrCoin (ZRC)">ZrCoin (ZRC)</option><option value="PutinCoin (PUT)">PutinCoin (PUT)</option><option value="Memetic / PepeCoin (MEME)">Memetic / PepeCoin (MEME)</option><option value="Riecoin (RIC)">Riecoin (RIC)</option><option value="ArtByte (ABY)">ArtByte (ABY)</option><option value="Spectrecoin (XSPEC)">Spectrecoin (XSPEC)</option><option value="ExclusiveCoin (EXCL)">ExclusiveCoin (EXCL)</option><option value="Phore (PHR)">Phore (PHR)</option><option value="Voise (VOISE)">Voise (VOISE)</option><option value="TrezarCoin (TZC)">TrezarCoin (TZC)</option><option value="HTMLCOIN (HTML5)">HTMLCOIN (HTML5)</option><option value="Qwark (QWARK)">Qwark (QWARK)</option><option value="Astro (ASTRO)">Astro (ASTRO)</option><option value="Bismuth (BIS)">Bismuth (BIS)</option><option value="DopeCoin (DOPE)">DopeCoin (DOPE)</option><option value="Circuits of Value (COVAL)">Circuits of Value (COVAL)</option><option value="AsiaCoin (AC)">AsiaCoin (AC)</option><option value="EverGreenCoin (EGC)">EverGreenCoin (EGC)</option><option value="APX (APX)">APX (APX)</option><option value="Karbowanec (KRB)">Karbowanec (KRB)</option><option value="Primecoin (XPM)">Primecoin (XPM)</option><option value="TrustPlus (TRUST)">TrustPlus (TRUST)</option><option value="Synergy (SNRG)">Synergy (SNRG)</option><option value="Sharechain (SSS)">Sharechain (SSS)</option><option value="TheGCCcoin (GCC)">TheGCCcoin (GCC)</option><option value="Universal Currency (UNIT)">Universal Currency (UNIT)</option><option value="Terracoin (TRC)">Terracoin (TRC)</option><option value="Bitswift (SWIFT)">Bitswift (SWIFT)</option><option value="Breakout Stake (BRX)">Breakout Stake (BRX)</option><option value="ChainCoin (CHC)">ChainCoin (CHC)</option><option value="EuropeCoin (ERC)">EuropeCoin (ERC)</option><option value="Pirl (PIRL)">Pirl (PIRL)</option><option value="Elixir (ELIX)">Elixir (ELIX)</option><option value="TrueFlip (TFL)">TrueFlip (TFL)</option><option value="2GIVE (2GIVE)">2GIVE (2GIVE)</option><option value="Divi (DIVX)">Divi (DIVX)</option><option value="GoldCoin (GLD)">GoldCoin (GLD)</option><option value="LIFE (LIFE)">LIFE (LIFE)</option><option value="Oceanlab (OCL)">Oceanlab (OCL)</option><option value="Project Decorum (PDC)">Project Decorum (PDC)</option><option value="GoByte (GBX)">GoByte (GBX)</option><option value="Darcrus (DAR)">Darcrus (DAR)</option><option value="Creditbit (CRB)">Creditbit (CRB)</option><option value="B2B (B2B)">B2B (B2B)</option><option value="Flixxo (FLIXX)">Flixxo (FLIXX)</option><option value="Propy (PRO)">Propy (PRO)</option><option value="Bela (BELA)">Bela (BELA)</option><option value="SuperCoin (SUPER)">SuperCoin (SUPER)</option><option value="Mercury Protocol (GMT)">Mercury Protocol (GMT)</option><option value="CannabisCoin (CANN)">CannabisCoin (CANN)</option><option value="MyBit Token (MYB)">MyBit Token (MYB)</option><option value="DCORP (DRP)">DCORP (DRP)</option><option value="CarTaxi Token (CTX)">CarTaxi Token (CTX)</option><option value="Bitcoin Red (BTCRED)">Bitcoin Red (BTCRED)</option><option value="vTorrent (VTR)">vTorrent (VTR)</option><option value="Creativecoin (CREA)">Creativecoin (CREA)</option><option value="vSlice (VSL)">vSlice (VSL)</option><option value="Blitzcash (BLITZ)">Blitzcash (BLITZ)</option><option value="Breakout (BRK)">Breakout (BRK)</option><option value="ParkByte (PKB)">ParkByte (PKB)</option><option value="Rupee (RUP)">Rupee (RUP)</option><option value="InflationCoin (IFLT)">InflationCoin (IFLT)</option><option value="GeoCoin (GEO)">GeoCoin (GEO)</option><option value="SHIELD (XSH)">SHIELD (XSH)</option><option value="MarteXcoin (MXT)">MarteXcoin (MXT)</option><option value="LUXCoin (LUX)">LUXCoin (LUX)</option><option value="Internxt (INXT)">Internxt (INXT)</option><option value="Innova (INN)">Innova (INN)</option><option value="Dotcoin (DOT)">Dotcoin (DOT)</option><option value="Atmos (ATMS)">Atmos (ATMS)</option><option value="Indorse Token (IND)">Indorse Token (IND)</option><option value="GoldBlocks (GB)">GoldBlocks (GB)</option><option value="Yocoin (YOC)">Yocoin (YOC)</option><option value="Aeron (ARN)">Aeron (ARN)</option><option value="HunterCoin (HUC)">HunterCoin (HUC)</option><option value="Zephyr (ZEPH)">Zephyr (ZEPH)</option><option value="Kolion (KLN)">Kolion (KLN)</option><option value="Startcoin (START)">Startcoin (START)</option><option value="HelloGold (HGT)">HelloGold (HGT)</option><option value="REAL (REAL)">REAL (REAL)</option><option value="e-Gulden (EFL)">e-Gulden (EFL)</option><option value="Ixcoin (IXC)">Ixcoin (IXC)</option><option value="Bulwark (BWK)">Bulwark (BWK)</option><option value="Autonio (NIO)">Autonio (NIO)</option><option value="Tokes (TKS)">Tokes (TKS)</option><option value="SpreadCoin (SPR)">SpreadCoin (SPR)</option><option value="ProCurrency (PROC)">ProCurrency (PROC)</option><option value="ZClassic (ZCL)">ZClassic (ZCL)</option><option value="Zennies (ZENI)">Zennies (ZENI)</option><option value="ATLANT (ATL)">ATLANT (ATL)</option><option value="BuzzCoin (BUZZ)">BuzzCoin (BUZZ)</option><option value="Hedge (HDG)">Hedge (HDG)</option><option value="Hush (HUSH)">Hush (HUSH)</option><option value="Ethbits (ETBS)">Ethbits (ETBS)</option><option value="VIVO (VIVO)">VIVO (VIVO)</option><option value="CHIPS (CHIPS)">CHIPS (CHIPS)</option><option value="Publica (PBL)">Publica (PBL)</option><option value="Quark (QRK)">Quark (QRK)</option><option value="VeriumReserve (VRM)">VeriumReserve (VRM)</option><option value="Magi (XMG)">Magi (XMG)</option><option value="Social (SCL)">Social (SCL)</option><option value="AdShares (ADST)">AdShares (ADST)</option><option value="Zoin (ZOI)">Zoin (ZOI)</option><option value="LuckChain (BASH)">LuckChain (BASH)</option><option value="XP (XP)">XP (XP)</option><option value="FLiK (FLIK)">FLiK (FLIK)</option><option value="DNotes (NOTE)">DNotes (NOTE)</option><option value="Unity Ingot (UNY)">Unity Ingot (UNY)</option><option value="AudioCoin (ADC)">AudioCoin (ADC)</option><option value="Megacoin (MEC)">Megacoin (MEC)</option><option value="REX (REX)">REX (REX)</option><option value="Rustbits (RUSTBITS)">Rustbits (RUSTBITS)</option><option value="Paccoin (PAC)">Paccoin (PAC)</option><option value="HyperStake (HYP)">HyperStake (HYP)</option><option value="SmartBillions (SMART)">SmartBillions (SMART)</option><option value="FlypMe (FYP)">FlypMe (FYP)</option><option value="FundYourselfNow (FYN)">FundYourselfNow (FYN)</option><option value="Woodcoin (LOG)">Woodcoin (LOG)</option><option value="WorldCoin (WDC)">WorldCoin (WDC)</option><option value="BitcoinZ (BTCZ)">BitcoinZ (BTCZ)</option><option value="GCoin (GCN)">GCoin (GCN)</option><option value="Cryptonite (XCN)">Cryptonite (XCN)</option><option value="UFO Coin (UFO)">UFO Coin (UFO)</option><option value="Opus (OPT)">Opus (OPT)</option><option value="Fastcoin (FST)">Fastcoin (FST)</option><option value="Tracto (TRCT)">Tracto (TRCT)</option><option value="PiplCoin (PIPL)">PiplCoin (PIPL)</option><option value="Fantomcoin (FCN)">Fantomcoin (FCN)</option><option value="Sumokoin (SUMO)">Sumokoin (SUMO)</option><option value="EquiTrader (EQT)">EquiTrader (EQT)</option><option value="Hubii Network (HBT)">Hubii Network (HBT)</option><option value="Elementrem (ELE)">Elementrem (ELE)</option><option value="Espers (ESP)">Espers (ESP)</option><option value="Anoncoin (ANC)">Anoncoin (ANC)</option><option value="eBoost (EBST)">eBoost (EBST)</option><option value="42-coin (42)">42-coin (42)</option><option value="Altcoin (ALT)">Altcoin (ALT)</option><option value="Canada eCoin (CDN)">Canada eCoin (CDN)</option><option value="Interstellar Holdings (HOLD)">Interstellar Holdings (HOLD)</option><option value="Ellaism (ELLA)">Ellaism (ELLA)</option><option value="DraftCoin (DFT)">DraftCoin (DFT)</option><option value="Intelligent Trading Tech (ITT)">Intelligent Trading Tech (ITT)</option><option value="Crypto Bullion (CBX)">Crypto Bullion (CBX)</option><option value="AltCommunity Coin (ALTCOM)">AltCommunity Coin (ALTCOM)</option><option value="Crystal Clear Token (CCT)">Crystal Clear Token (CCT)</option><option value="KuCoin (KCS)">KuCoin (KCS)</option><option value="Rebellious (REBL)">Rebellious (REBL)</option><option value="Nuls (NULS)">Nuls (NULS)</option><option value="Upfiring (UFR)">Upfiring (UFR)</option><option value="ELTCOIN (ELTCOIN)">ELTCOIN (ELTCOIN)</option><option value="Everus (EVR)">Everus (EVR)</option><option value="Senderon (SDRN)">Senderon (SDRN)</option><option value="ASH (QASH)">ASH (QASH)</option><option value="Payfair (PFR)">Payfair (PFR)</option><option value="AdCoin (ACC)">AdCoin (ACC)</option><option value="BlakeStar (BLAS)">BlakeStar (BLAS)</option><option value="Oyster Pearl (PRL)">Oyster Pearl (PRL)</option><option value="LockChain (LOC)">LockChain (LOC)</option><option value="MediBond (MEDI)">MediBond (MEDI)</option><option value="CampusCoin (CMPCO)">CampusCoin (CMPCO)</option><option value="MonacoCoin (XMCC)">MonacoCoin (XMCC)</option><option value="PoSToken (POS)">PoSToken (POS)</option><option value="Kittehcoin (MEOW)">Kittehcoin (MEOW)</option><option value="Octanox (OTX)">Octanox (OTX)</option></select>
                </div>

                <div class="form-group">
                    <label>Is:</label>
                    <div class="error"></div>
                    <select id="new_alert_form_type" name="new_alert_form[type][]" required="required" class="selectpicker form-control" title="Select type(s)" tabindex="2" id="recipient-type" multiple="multiple"><option value="add">Added</option><option value="hot">Hot</option></select>
                </div>

                <div class="form-group">
                    <label style="color: red;" for="recipient-mail" class="control-label">*</label> <label>My email:</label>
                    <div class="error"></div>
                    <input type="email" id="new_alert_form_email" name="new_alert_form[email]" required="required" class="form-control" tabindex="3" id="recipient-mail" />
                </div>

                <div class="form-group">
                    <div id="recaptchaAlert"></div>
                </div>
            </div>
            <div class="modal-footer">
                <div class="row">
                    <div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
                        <span class="alertInfo">Free, no spam, easy to unsubscribe</span>
                    </div>
                    <div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        <button type="submit" id="new_alert_form_submit" name="new_alert_form[submit]" class="btn btn-d btn-round" tabindex="4">Create</button>
                    </div>
                </div>
            </div>
            <input type="hidden" id="new_alert_form__token" name="new_alert_form[_token]" value="f5Zfl0ECQr1vtYyZR9oU0SexD_DQM8-LeW9D9COMJgs" />
    </form>
        </div>
    </div>
</div>
                <div class="modal fade" id="alertReminder" tabindex="-1" role="dialog" aria-labelledby="alertReminder">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        <h4 class="modal-title" id="exampleModalLabel">Create your reminder</h4>
                    </div>
                    <form name="form" method="post" class="form" role="form" id="form_alert_add">
                    <div class="modal-body">


                        <div class="form-group">
                            <label style="font-weight: normal"><strong>Event:</strong> <span id="remindereventdate"></span> - <span id="remindereventcoin"></span> - <span id="remindereventtitle"></span></label>
                        </div>
                        <div class="form-group">
                            <label>I want to be reminded:</label>
                            <div class="error"></div>
                            <select id="form_frequency" name="form[frequency][]" required="required" class="selectpicker form-control" tabindex="1" id="recipient-frequency" multiple="multiple"><option value="1">1 day prior to the event</option><option value="2">2 days prior to the event</option><option value="3">3 days prior to the event</option><option value="4">4 days prior to the event</option><option value="5">5 days prior to the event</option><option value="6">6 days prior to the event</option><option value="7">7 days prior to the event</option><option value="8">8 days prior to the event</option><option value="9">9 days prior to the event</option><option value="10">10 days prior to the event</option><option value="11">11 days prior to the event</option><option value="12">12 days prior to the event</option><option value="13">13 days prior to the event</option><option value="14">14 days prior to the event</option></select>
                        </div>

                        <div class="form-group">
                            <label>My email:</label>
                            <div class="error"></div>
                            <input type="email" id="form_email" name="form[email]" required="required" class="form-control" tabindex="2" id="recipient-reminder-mail" />
                        </div>

                        <div class="form-group">
                            <input type="hidden" id="form_event_id" name="form[event_id]" required="required" />
                        </div>

                        <div class="form-group">
                            <div id="recaptchaReminder"></div>
                        </div>
                    </div>

                    <div class="modal-footer">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
                                <span class="alertInfo">Free, no spam, easy to unsubscribe</span>
                            </div>
                            <div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                <button type="submit" id="form_submit" name="form[submit]" class="btn btn-d btn-round" tabindex="3">Create</button>
                            </div>
                        </div>
                    </div>
                    <input type="hidden" id="form__token" name="form[_token]" value="3wlKJWMCnG-FGO7q4xJy8BXbzJcVNr5l95Yugd6QfpI" />
    </form>
                </div>
            </div>
        </div>

    <section class="module-extra-small header">
        <div class="titan-caption">
            <div class="caption-content">
                <div class="font-alt mb-30 titan-title-size-3"><a href="/">Cryptocurrency Calendar</a></div>
                <div class="font-alt mb-20 titan-title-size-1">Evidence-based & Community-driven</div>
                    <div class="container">
        <a class="section-scroll btn btn-border-w btn-round btn-home" href="#explore"><i class="fa fa-search" aria-hidden="true"></i> Explore Events</a>
        <a class="btn btn-border-w btn-round btn-home" href="/add"><i class="fa fa-plus" aria-hidden="true"></i> Add Event</a>
        <span class="separator">|</span>
        <a class="btn btn-border-w btn-round btn-home" href="#alertModal" data-toggle="modal" data-target="#alertModal"><i class="fa fa-bell-o" aria-hidden="true"></i> Create alert</a>
    </div>

            </div>
        </div>
    </section>

    <div class="main showcase-page">
            <section class="module-extra-small" id="explore">

        <div class="container">
    <div class="row text-center" style="margin-bottom: 20px;">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <div class="banner_medium">
                <span id="ct_IxByie"></span>
                                <div id="bsap_1307564" class="bsarocks bsap_bc77aad56a362813160c5f60585b9b56"></div>
            </div>
        </div>
    </div>
</div>

        <div class="container">


                                    <div>
                <ul class="nav nav-tabs font-alt">
                    <li ><a href="/pastevents"><strong>Past Events</strong></a></li>
                    <li  class="active"><a href="/"><strong>Upcoming Events</strong></a></li>
                </ul>
                <div class="filter">
                    <div class="container">
                        <form name="form" method="get" class="form" role="form">




                        <select id="form_month" name="form[month]" class="selectpicker btn-home" data-width="fit" title="Month" tabindex="1"><option value=""></option><option value="01">January</option><option value="02">February</option><option value="03">March</option><option value="04">April</option><option value="05">May</option><option value="06">June</option><option value="07">July</option><option value="08">August</option><option value="09">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select>


                        <select id="form_year" name="form[year]" class="selectpicker btn-home" data-width="fit" title="Year" tabindex="2"><option value=""></option><option value="2017">2017</option><option value="2018">2018</option><option value="2019">2019</option></select>


                        <select id="form_coin" name="form[coin][]" class="selectpicker btn-home" data-live-search="true" data-width="160" data-selected-text-format="count &gt; 2" title="Coin" tabindex="3" multiple="multiple"><option value="Bitcoin (BTC)">Bitcoin (BTC)</option><option value="Ethereum (ETH)">Ethereum (ETH)</option><option value="Bitcoin Cash (BCH)">Bitcoin Cash (BCH)</option><option value="IOTA (MIOTA)">IOTA (MIOTA)</option><option value="Ripple (XRP)">Ripple (XRP)</option><option value="Litecoin (LTC)">Litecoin (LTC)</option><option value="Dash (DASH)">Dash (DASH)</option><option value="Bitcoin Gold (BTG)">Bitcoin Gold (BTG)</option><option value="Monero (XMR)">Monero (XMR)</option><option value="NEM (XEM)">NEM (XEM)</option><option value="Cardano (ADA)">Cardano (ADA)</option><option value="Ethereum Classic (ETC)">Ethereum Classic (ETC)</option><option value="Stellar Lumens (XLM)">Stellar Lumens (XLM)</option><option value="NEO (NEO)">NEO (NEO)</option><option value="EOS (EOS)">EOS (EOS)</option><option value="BitConnect (BCC)">BitConnect (BCC)</option><option value="Populous (PPT)">Populous (PPT)</option><option value="Waves (WAVES)">Waves (WAVES)</option><option value="Lisk (LSK)">Lisk (LSK)</option><option value="Stratis (STRAT)">Stratis (STRAT)</option><option value="Qtum (QTUM)">Qtum (QTUM)</option><option value="Zcash (ZEC)">Zcash (ZEC)</option><option value="OmiseGO (OMG)">OmiseGO (OMG)</option><option value="Tether (USDT)">Tether (USDT)</option><option value="MonaCoin (MONA)">MonaCoin (MONA)</option><option value="Hshare (HSR)">Hshare (HSR)</option><option value="Nxt (NXT)">Nxt (NXT)</option><option value="Ardor (ARDR)">Ardor (ARDR)</option><option value="Bytecoin (BCN)">Bytecoin (BCN)</option><option value="BitShares (BTS)">BitShares (BTS)</option><option value="Steem (STEEM)">Steem (STEEM)</option><option value="SALT (SALT)">SALT (SALT)</option><option value="Einsteinium (EMC2)">Einsteinium (EMC2)</option><option value="Decred (DCR)">Decred (DCR)</option><option value="Ark (ARK)">Ark (ARK)</option><option value="Vertcoin (VTC)">Vertcoin (VTC)</option><option value="Veritaseum (VERI)">Veritaseum (VERI)</option><option value="Augur (REP)">Augur (REP)</option><option value="Komodo (KMD)">Komodo (KMD)</option><option value="TRON (TRX)">TRON (TRX)</option><option value="Dogecoin (DOGE)">Dogecoin (DOGE)</option><option value="Siacoin (SC)">Siacoin (SC)</option><option value="Binance Coin (BNB)">Binance Coin (BNB)</option><option value="Golem (GNT)">Golem (GNT)</option><option value="QASH (QASH)">QASH (QASH)</option><option value="PIVX (PIVX)">PIVX (PIVX)</option><option value="Santiment Network Token (SAN)">Santiment Network Token (SAN)</option><option value="TenX (PAY)">TenX (PAY)</option><option value="MaidSafeCoin (MAID)">MaidSafeCoin (MAID)</option><option value="Status (SNT)">Status (SNT)</option><option value="DigixDAO (DGD)">DigixDAO (DGD)</option><option value="Byteball Bytes (GBYTE)">Byteball Bytes (GBYTE)</option><option value="Exchange Union (XUC)">Exchange Union (XUC)</option><option value="Cryptonex (CNX)">Cryptonex (CNX)</option><option value="Basic Attention Token (BAT)">Basic Attention Token (BAT)</option><option value="Power Ledger (POWR)">Power Ledger (POWR)</option><option value="Walton (WTC)">Walton (WTC)</option><option value="BitcoinDark (BTCD)">BitcoinDark (BTCD)</option><option value="Factom (FCT)">Factom (FCT)</option><option value="Syscoin (SYS)">Syscoin (SYS)</option><option value="Decentraland (MANA)">Decentraland (MANA)</option><option value="Kyber Network (KNC)">Kyber Network (KNC)</option><option value="Bytom (BTM)">Bytom (BTM)</option><option value="Pura (PURA)">Pura (PURA)</option><option value="Monaco (MCO)">Monaco (MCO)</option><option value="Raiden Network Token (RDN)">Raiden Network Token (RDN)</option><option value="Gas (GAS)">Gas (GAS)</option><option value="ZCoin (XZC)">ZCoin (XZC)</option><option value="Aeternity (AE)">Aeternity (AE)</option><option value="Iconomi (ICN)">Iconomi (ICN)</option><option value="VeChain (VEN)">VeChain (VEN)</option><option value="GameCredits (GAME)">GameCredits (GAME)</option><option value="DigiByte (DGB)">DigiByte (DGB)</option><option value="RaiBlocks (XRB)">RaiBlocks (XRB)</option><option value="FunFair (FUN)">FunFair (FUN)</option><option value="Verge (XVG)">Verge (XVG)</option><option value="Gnosis (GNO)">Gnosis (GNO)</option><option value="Nexus (NXS)">Nexus (NXS)</option><option value="0x (ZRX)">0x (ZRX)</option><option value="Request Network (REQ)">Request Network (REQ)</option><option value="Blocknet (BLOCK)">Blocknet (BLOCK)</option><option value="Bancor (BNT)">Bancor (BNT)</option><option value="Dragonchain (DRGN)">Dragonchain (DRGN)</option><option value="Metal (MTL)">Metal (MTL)</option><option value="Civic (CVC)">Civic (CVC)</option><option value="Skycoin (SKY)">Skycoin (SKY)</option><option value="Ethos (ETHOS)">Ethos (ETHOS)</option><option value="ChainLink (LINK)">ChainLink (LINK)</option><option value="Edgeless (EDG)">Edgeless (EDG)</option><option value="Aion (AION)">Aion (AION)</option><option value="NAV Coin (NAV)">NAV Coin (NAV)</option><option value="Storj (STORJ)">Storj (STORJ)</option><option value="GXShares (GXS)">GXShares (GXS)</option><option value="Streamr DATAcoin (DATA)">Streamr DATAcoin (DATA)</option><option value="Metaverse ETP (ETP)">Metaverse ETP (ETP)</option><option value="ATMChain (ATM)">ATMChain (ATM)</option><option value="RChain (RHOC)">RChain (RHOC)</option><option value="Jinn (JINN)">Jinn (JINN)</option><option value="MinexCoin (MNX)">MinexCoin (MNX)</option><option value="Achain (ACT)">Achain (ACT)</option><option value="Substratum (SUB)">Substratum (SUB)</option><option value="Revain (R)">Revain (R)</option><option value="Peercoin (PPC)">Peercoin (PPC)</option><option value="Pepe Cash (PEPECASH)">Pepe Cash (PEPECASH)</option><option value="Lykke (LKK)">Lykke (LKK)</option><option value="Groestlcoin (GRS)">Groestlcoin (GRS)</option><option value="BitBay (BAY)">BitBay (BAY)</option><option value="ZenCash (ZEN)">ZenCash (ZEN)</option><option value="AdEx (ADX)">AdEx (ADX)</option><option value="SingularDTV (SNGLS)">SingularDTV (SNGLS)</option><option value="Ubiq (UBQ)">Ubiq (UBQ)</option><option value="MobileGo (MGO)">MobileGo (MGO)</option><option value="Feathercoin (FTC)">Feathercoin (FTC)</option><option value="Quantstamp (QSP)">Quantstamp (QSP)</option><option value="PotCoin (POT)">PotCoin (POT)</option><option value="Particl (PART)">Particl (PART)</option><option value="Aragon (ANT)">Aragon (ANT)</option><option value="YOYOW (YOYOW)">YOYOW (YOYOW)</option><option value="FairCoin (FAIR)">FairCoin (FAIR)</option><option value="Loopring (LRC)">Loopring (LRC)</option><option value="Asch (XAS)">Asch (XAS)</option><option value="Cobinhood (COB)">Cobinhood (COB)</option><option value="Quantum Resistant Ledger (QRL)">Quantum Resistant Ledger (QRL)</option><option value="Ripio Credit Network (RCN)">Ripio Credit Network (RCN)</option><option value="PayPie (PPP)">PayPie (PPP)</option><option value="Counterparty (XCP)">Counterparty (XCP)</option><option value="Ink (INK)">Ink (INK)</option><option value="Open Trading Network (OTN)">Open Trading Network (OTN)</option><option value="Aeon (AEON)">Aeon (AEON)</option><option value="Viacoin (VIA)">Viacoin (VIA)</option><option value="Agoras Tokens (AGRS)">Agoras Tokens (AGRS)</option><option value="Mercury (MER)">Mercury (MER)</option><option value="FedoraCoin (TIPS)">FedoraCoin (TIPS)</option><option value="Eidoo (EDO)">Eidoo (EDO)</option><option value="SONM (SNM)">SONM (SNM)</option><option value="Wings (WINGS)">Wings (WINGS)</option><option value="ReddCoin (RDD)">ReddCoin (RDD)</option><option value="Kin (KIN)">Kin (KIN)</option><option value="Melon (MLN)">Melon (MLN)</option><option value="Neblio (NEBL)">Neblio (NEBL)</option><option value="KuCoin Shares (KCS)">KuCoin Shares (KCS)</option><option value="WeTrust (TRST)">WeTrust (TRST)</option><option value="Blocktix (TIX)">Blocktix (TIX)</option><option value="Russian Miner Coin (RMC)">Russian Miner Coin (RMC)</option><option value="Rise (RISE)">Rise (RISE)</option><option value="iExec RLC (RLC)">iExec RLC (RLC)</option><option value="Diamond (DMD)">Diamond (DMD)</option><option value="Emercoin (EMC)">Emercoin (EMC)</option><option value="Voxels (VOX)">Voxels (VOX)</option><option value="Namecoin (NMC)">Namecoin (NMC)</option><option value="Enigma (ENG)">Enigma (ENG)</option><option value="Safe Exchange Coin (SAFEX)">Safe Exchange Coin (SAFEX)</option><option value="BLOCKv (VEE)">BLOCKv (VEE)</option><option value="Wagerr (WGR)">Wagerr (WGR)</option><option value="Zeusshield (ZSC)">Zeusshield (ZSC)</option><option value="CloakCoin (CLOAK)">CloakCoin (CLOAK)</option><option value="SIBCoin (SIB)">SIBCoin (SIB)</option><option value="TaaS (TAAS)">TaaS (TAAS)</option><option value="WhiteCoin (XWC)">WhiteCoin (XWC)</option><option value="Bitcore (BTX)">Bitcore (BTX)</option><option value="AirSwap (AST)">AirSwap (AST)</option><option value="CoinDash (CDT)">CoinDash (CDT)</option><option value="SmartCash (SMART)">SmartCash (SMART)</option><option value="Pillar (PLR)">Pillar (PLR)</option><option value="NoLimitCoin (NLC2)">NoLimitCoin (NLC2)</option><option value="Cofound.it (CFI)">Cofound.it (CFI)</option><option value="Tierion (TNT)">Tierion (TNT)</option><option value="I/O Coin (IOC)">I/O Coin (IOC)</option><option value="Enjin Coin (ENJ)">Enjin Coin (ENJ)</option><option value="DECENT (DCT)">DECENT (DCT)</option><option value="Gulden (NLG)">Gulden (NLG)</option><option value="Crown (CRW)">Crown (CRW)</option><option value="bitqy (BQ)">bitqy (BQ)</option><option value="Modum (MOD)">Modum (MOD)</option><option value="OKCash (OK)">OKCash (OK)</option><option value="Time New Bank (TNB)">Time New Bank (TNB)</option><option value="Presearch (PRE)">Presearch (PRE)</option><option value="SaluS (SLS)">SaluS (SLS)</option><option value="Numeraire (NMR)">Numeraire (NMR)</option><option value="Paypex (PAYX)">Paypex (PAYX)</option><option value="Cindicator (CND)">Cindicator (CND)</option><option value="FirstBlood (1ST)">FirstBlood (1ST)</option><option value="Ambrosus (AMB)">Ambrosus (AMB)</option><option value="Bitzeny (ZNY)">Bitzeny (ZNY)</option><option value="Centra (CTR)">Centra (CTR)</option><option value="LBRY Credits (LBC)">LBRY Credits (LBC)</option><option value="Delphy (DPY)">Delphy (DPY)</option><option value="Steem Dollars (SBD)">Steem Dollars (SBD)</option><option value="XTRABYTES (XBY)">XTRABYTES (XBY)</option><option value="BitDice (CSNO)">BitDice (CSNO)</option><option value="GridCoin (GRC)">GridCoin (GRC)</option><option value="Burst (BURST)">Burst (BURST)</option><option value="ION (ION)">ION (ION)</option><option value="Moeda Loyalty Points (MDA)">Moeda Loyalty Points (MDA)</option><option value="district0x (DNT)">district0x (DNT)</option><option value="Grid+ (GRID)">Grid+ (GRID)</option><option value="Triggers (TRIG)">Triggers (TRIG)</option><option value="Dentacoin (DCN)">Dentacoin (DCN)</option><option value="Matchpool (GUP)">Matchpool (GUP)</option><option value="Global Currency Reserve (GCR)">Global Currency Reserve (GCR)</option><option value="Waves Community Token (WCT)">Waves Community Token (WCT)</option><option value="Shift (SHIFT)">Shift (SHIFT)</option><option value="Golos (GOLOS)">Golos (GOLOS)</option><option value="Unikoin Gold (UKG)">Unikoin Gold (UKG)</option><option value="BlackCoin (BLK)">BlackCoin (BLK)</option><option value="ClearPoll (POLL)">ClearPoll (POLL)</option><option value="Boolberry (BBR)">Boolberry (BBR)</option><option value="Xaurum (XAUR)">Xaurum (XAUR)</option><option value="Dimecoin (DIME)">Dimecoin (DIME)</option><option value="Polybius (PLBT)">Polybius (PLBT)</option><option value="TransferCoin (TX)">TransferCoin (TX)</option><option value="LEOcoin (LEO)">LEOcoin (LEO)</option><option value="ICOS (ICOS)">ICOS (ICOS)</option><option value="Dent (DENT)">Dent (DENT)</option><option value="Aventus (AVT)">Aventus (AVT)</option><option value="HempCoin (THC)">HempCoin (THC)</option><option value="Omni (OMNI)">Omni (OMNI)</option><option value="Humaniq (HMQ)">Humaniq (HMQ)</option><option value="EncrypGen (DNA)">EncrypGen (DNA)</option><option value="SpankChain (SPANK)">SpankChain (SPANK)</option><option value="XPlay (XPA)">XPlay (XPA)</option><option value="MonetaryUnit (MUE)">MonetaryUnit (MUE)</option><option value="Elastic (XEL)">Elastic (XEL)</option><option value="ETHLend (LEND)">ETHLend (LEND)</option><option value="Red Pulse (RPX)">Red Pulse (RPX)</option><option value="Etherparty (FUEL)">Etherparty (FUEL)</option><option value="Synereo (AMP)">Synereo (AMP)</option><option value="iXledger (IXT)">iXledger (IXT)</option><option value="Po.et (POE)">Po.et (POE)</option><option value="Rubycoin (RBY)">Rubycoin (RBY)</option><option value="DigitalNote (XDN)">DigitalNote (XDN)</option><option value="ATBCoin (ATB)">ATBCoin (ATB)</option><option value="TokenCard (TKN)">TokenCard (TKN)</option><option value="Stox (STX)">Stox (STX)</option><option value="Genesis Vision (GVT)">Genesis Vision (GVT)</option><option value="Paragon (PRG)">Paragon (PRG)</option><option value="Viberate (VIB)">Viberate (VIB)</option><option value="Clams (CLAM)">Clams (CLAM)</option><option value="Everex (EVX)">Everex (EVX)</option><option value="Rialto (XRL)">Rialto (XRL)</option><option value="Agrello (DLT)">Agrello (DLT)</option><option value="SolarCoin (SLR)">SolarCoin (SLR)</option><option value="Hive (HVN)">Hive (HVN)</option><option value="SunContract (SNC)">SunContract (SNC)</option><option value="OBITS (OBITS)">OBITS (OBITS)</option><option value="Monetha (MTH)">Monetha (MTH)</option><option value="Etheroll (DICE)">Etheroll (DICE)</option><option value="BitSend (BSD)">BitSend (BSD)</option><option value="The ChampCoin (TCC)">The ChampCoin (TCC)</option><option value="CasinoCoin (CSC)">CasinoCoin (CSC)</option><option value="Gambit (GAM)">Gambit (GAM)</option><option value="Sphere (SPHR)">Sphere (SPHR)</option><option value="ALIS (ALIS)">ALIS (ALIS)</option><option value="BridgeCoin (BCO)">BridgeCoin (BCO)</option><option value="Radium (RADS)">Radium (RADS)</option><option value="Nimiq (NET)">Nimiq (NET)</option><option value="Databits (DTB)">Databits (DTB)</option><option value="Target Coin (TGT)">Target Coin (TGT)</option><option value="NeosCoin (NEOS)">NeosCoin (NEOS)</option><option value="Pascal Coin (PASC)">Pascal Coin (PASC)</option><option value="Unobtanium (UNO)">Unobtanium (UNO)</option><option value="Oxycoin (OXY)">Oxycoin (OXY)</option><option value="bitCNY (BITCNY)">bitCNY (BITCNY)</option><option value="NVO (NVST)">NVO (NVST)</option><option value="Peerplays (PPY)">Peerplays (PPY)</option><option value="OracleChain (OCT)">OracleChain (OCT)</option><option value="adToken (ADT)">adToken (ADT)</option><option value="Soarcoin (SOAR)">Soarcoin (SOAR)</option><option value="VeriCoin (VRC)">VeriCoin (VRC)</option><option value="BCAP (BCAP)">BCAP (BCAP)</option><option value="Expanse (EXP)">Expanse (EXP)</option><option value="Mothership (MSP)">Mothership (MSP)</option><option value="Bitdeal (BDL)">Bitdeal (BDL)</option><option value="Centurion (CNT)">Centurion (CNT)</option><option value="Vcash (XVC)">Vcash (XVC)</option><option value="Xenon (XNN)">Xenon (XNN)</option><option value="FoldingCoin (FLDC)">FoldingCoin (FLDC)</option><option value="KickCoin (KICK)">KickCoin (KICK)</option><option value="Primas (PST)">Primas (PST)</option><option value="DeepOnion (ONION)">DeepOnion (ONION)</option><option value="Tao (XTO)">Tao (XTO)</option><option value="FlorinCoin (FLO)">FlorinCoin (FLO)</option><option value="NuShares (NSR)">NuShares (NSR)</option><option value="DomRaider (DRT)">DomRaider (DRT)</option><option value="Mysterium (MYST)">Mysterium (MYST)</option><option value="InvestFeed (IFT)">InvestFeed (IFT)</option><option value="MCAP (MCAP)">MCAP (MCAP)</option><option value="Rivetz (RVT)">Rivetz (RVT)</option><option value="Energycoin (ENRG)">Energycoin (ENRG)</option><option value="ToaCoin (TOA)">ToaCoin (TOA)</option><option value="LoMoCoin (LMC)">LoMoCoin (LMC)</option><option value="Blackmoon Crypto (BMC)">Blackmoon Crypto (BMC)</option><option value="Chronobank (TIME)">Chronobank (TIME)</option><option value="Lunyr (LUN)">Lunyr (LUN)</option><option value="HEAT (HEAT)">HEAT (HEAT)</option><option value="Swarm City (SWT)">Swarm City (SWT)</option><option value="Patientory (PTOY)">Patientory (PTOY)</option><option value="Nexium (NXC)">Nexium (NXC)</option><option value="Obsidian (ODN)">Obsidian (ODN)</option><option value="BitBean (BITB)">BitBean (BITB)</option><option value="Bitcloud (BTDX)">Bitcloud (BTDX)</option><option value="Change (CAG)">Change (CAG)</option><option value="Bitmark (BTM)">Bitmark (BTM)</option><option value="Masternodecoin (MTNC)">Masternodecoin (MTNC)</option><option value="Novacoin (NVC)">Novacoin (NVC)</option><option value="Curecoin (CURE)">Curecoin (CURE)</option><option value="Maecenas (ART)">Maecenas (ART)</option><option value="Decision Token (HST)">Decision Token (HST)</option><option value="BlockCAT (CAT)">BlockCAT (CAT)</option><option value="Incent (INCNT)">Incent (INCNT)</option><option value="Sequence (SEQ)">Sequence (SEQ)</option><option value="eBitcoin (EBTC)">eBitcoin (EBTC)</option><option value="DubaiCoin (DBIX)">DubaiCoin (DBIX)</option><option value="AirToken (AIR)">AirToken (AIR)</option><option value="bitUSD (BITUSD)">bitUSD (BITUSD)</option><option value="Credo (CREDO)">Credo (CREDO)</option><option value="PRIZM (PZM)">PRIZM (PZM)</option><option value="EncryptoTel [WAVES] (ETT)">EncryptoTel [WAVES] (ETT)</option><option value="Quantum (QAU)">Quantum (QAU)</option><option value="DecentBet (DBET)">DecentBet (DBET)</option><option value="PinkCoin (PINK)">PinkCoin (PINK)</option><option value="OAX (OAX)">OAX (OAX)</option><option value="Auroracoin (AUR)">Auroracoin (AUR)</option><option value="Mooncoin (MOON)">Mooncoin (MOON)</option><option value="BLUE (BLUE)">BLUE (BLUE)</option><option value="COSS (COSS)">COSS (COSS)</option><option value="Onix (ONX)">Onix (ONX)</option><option value="Bitcrystals (BCY)">Bitcrystals (BCY)</option><option value="PoSW Coin (POSW)">PoSW Coin (POSW)</option><option value="Bitcoin Plus (XBC)">Bitcoin Plus (XBC)</option><option value="Dynamic (DYN)">Dynamic (DYN)</option><option value="Pluton (PLU)">Pluton (PLU)</option><option value="Musicoin (MUSIC)">Musicoin (MUSIC)</option><option value="Pesetacoin (PTC)">Pesetacoin (PTC)</option><option value="DAO.Casino (BET)">DAO.Casino (BET)</option><option value="Stealthcoin (XST)">Stealthcoin (XST)</option><option value="Ethereum Movie Venture (EMV)">Ethereum Movie Venture (EMV)</option><option value="E-Dinar Coin (EDR)">E-Dinar Coin (EDR)</option><option value="Internet of People (IOP)">Internet of People (IOP)</option><option value="Primalbase Token (PBT)">Primalbase Token (PBT)</option><option value="BlockMason Credit Protocol (BCPT)">BlockMason Credit Protocol (BCPT)</option><option value="BlueCoin (BLU)">BlueCoin (BLU)</option><option value="EarthCoin (EAC)">EarthCoin (EAC)</option><option value="ECC (ECC)">ECC (ECC)</option><option value="Syndicate (SYNX)">Syndicate (SYNX)</option><option value="Myriad (XMY)">Myriad (XMY)</option><option value="VIBE (VIBE)">VIBE (VIBE)</option><option value="Sexcoin (SXC)">Sexcoin (SXC)</option><option value="CVCoin (CVCOIN)">CVCoin (CVCOIN)</option><option value="Neutron (NTRN)">Neutron (NTRN)</option><option value="CryptoPing (PING)">CryptoPing (PING)</option><option value="Dovu (DOVU)">Dovu (DOVU)</option><option value="Mintcoin (MINT)">Mintcoin (MINT)</option><option value="Kore (KORE)">Kore (KORE)</option><option value="Lampix (PIX)">Lampix (PIX)</option><option value="LAToken (LA)">LAToken (LA)</option><option value="NewYorkCoin (NYC)">NewYorkCoin (NYC)</option><option value="Bankcoin (B@)">Bankcoin (B@)</option><option value="ZrCoin (ZRC)">ZrCoin (ZRC)</option><option value="PutinCoin (PUT)">PutinCoin (PUT)</option><option value="Memetic / PepeCoin (MEME)">Memetic / PepeCoin (MEME)</option><option value="Riecoin (RIC)">Riecoin (RIC)</option><option value="ArtByte (ABY)">ArtByte (ABY)</option><option value="Spectrecoin (XSPEC)">Spectrecoin (XSPEC)</option><option value="ExclusiveCoin (EXCL)">ExclusiveCoin (EXCL)</option><option value="Phore (PHR)">Phore (PHR)</option><option value="Voise (VOISE)">Voise (VOISE)</option><option value="TrezarCoin (TZC)">TrezarCoin (TZC)</option><option value="HTMLCOIN (HTML5)">HTMLCOIN (HTML5)</option><option value="Qwark (QWARK)">Qwark (QWARK)</option><option value="Astro (ASTRO)">Astro (ASTRO)</option><option value="Bismuth (BIS)">Bismuth (BIS)</option><option value="DopeCoin (DOPE)">DopeCoin (DOPE)</option><option value="Circuits of Value (COVAL)">Circuits of Value (COVAL)</option><option value="AsiaCoin (AC)">AsiaCoin (AC)</option><option value="EverGreenCoin (EGC)">EverGreenCoin (EGC)</option><option value="APX (APX)">APX (APX)</option><option value="Karbowanec (KRB)">Karbowanec (KRB)</option><option value="Primecoin (XPM)">Primecoin (XPM)</option><option value="TrustPlus (TRUST)">TrustPlus (TRUST)</option><option value="Synergy (SNRG)">Synergy (SNRG)</option><option value="Sharechain (SSS)">Sharechain (SSS)</option><option value="TheGCCcoin (GCC)">TheGCCcoin (GCC)</option><option value="Universal Currency (UNIT)">Universal Currency (UNIT)</option><option value="Terracoin (TRC)">Terracoin (TRC)</option><option value="Bitswift (SWIFT)">Bitswift (SWIFT)</option><option value="Breakout Stake (BRX)">Breakout Stake (BRX)</option><option value="ChainCoin (CHC)">ChainCoin (CHC)</option><option value="EuropeCoin (ERC)">EuropeCoin (ERC)</option><option value="Pirl (PIRL)">Pirl (PIRL)</option><option value="Elixir (ELIX)">Elixir (ELIX)</option><option value="TrueFlip (TFL)">TrueFlip (TFL)</option><option value="2GIVE (2GIVE)">2GIVE (2GIVE)</option><option value="Divi (DIVX)">Divi (DIVX)</option><option value="GoldCoin (GLD)">GoldCoin (GLD)</option><option value="LIFE (LIFE)">LIFE (LIFE)</option><option value="Oceanlab (OCL)">Oceanlab (OCL)</option><option value="Project Decorum (PDC)">Project Decorum (PDC)</option><option value="GoByte (GBX)">GoByte (GBX)</option><option value="Darcrus (DAR)">Darcrus (DAR)</option><option value="Creditbit (CRB)">Creditbit (CRB)</option><option value="B2B (B2B)">B2B (B2B)</option><option value="Flixxo (FLIXX)">Flixxo (FLIXX)</option><option value="Propy (PRO)">Propy (PRO)</option><option value="Bela (BELA)">Bela (BELA)</option><option value="SuperCoin (SUPER)">SuperCoin (SUPER)</option><option value="Mercury Protocol (GMT)">Mercury Protocol (GMT)</option><option value="CannabisCoin (CANN)">CannabisCoin (CANN)</option><option value="MyBit Token (MYB)">MyBit Token (MYB)</option><option value="DCORP (DRP)">DCORP (DRP)</option><option value="CarTaxi Token (CTX)">CarTaxi Token (CTX)</option><option value="Bitcoin Red (BTCRED)">Bitcoin Red (BTCRED)</option><option value="vTorrent (VTR)">vTorrent (VTR)</option><option value="Creativecoin (CREA)">Creativecoin (CREA)</option><option value="vSlice (VSL)">vSlice (VSL)</option><option value="Blitzcash (BLITZ)">Blitzcash (BLITZ)</option><option value="Breakout (BRK)">Breakout (BRK)</option><option value="ParkByte (PKB)">ParkByte (PKB)</option><option value="Rupee (RUP)">Rupee (RUP)</option><option value="InflationCoin (IFLT)">InflationCoin (IFLT)</option><option value="GeoCoin (GEO)">GeoCoin (GEO)</option><option value="SHIELD (XSH)">SHIELD (XSH)</option><option value="MarteXcoin (MXT)">MarteXcoin (MXT)</option><option value="LUXCoin (LUX)">LUXCoin (LUX)</option><option value="Internxt (INXT)">Internxt (INXT)</option><option value="Innova (INN)">Innova (INN)</option><option value="Dotcoin (DOT)">Dotcoin (DOT)</option><option value="Atmos (ATMS)">Atmos (ATMS)</option><option value="Indorse Token (IND)">Indorse Token (IND)</option><option value="GoldBlocks (GB)">GoldBlocks (GB)</option><option value="Yocoin (YOC)">Yocoin (YOC)</option><option value="Aeron (ARN)">Aeron (ARN)</option><option value="HunterCoin (HUC)">HunterCoin (HUC)</option><option value="Zephyr (ZEPH)">Zephyr (ZEPH)</option><option value="Kolion (KLN)">Kolion (KLN)</option><option value="Startcoin (START)">Startcoin (START)</option><option value="HelloGold (HGT)">HelloGold (HGT)</option><option value="REAL (REAL)">REAL (REAL)</option><option value="e-Gulden (EFL)">e-Gulden (EFL)</option><option value="Ixcoin (IXC)">Ixcoin (IXC)</option><option value="Bulwark (BWK)">Bulwark (BWK)</option><option value="Autonio (NIO)">Autonio (NIO)</option><option value="Tokes (TKS)">Tokes (TKS)</option><option value="SpreadCoin (SPR)">SpreadCoin (SPR)</option><option value="ProCurrency (PROC)">ProCurrency (PROC)</option><option value="ZClassic (ZCL)">ZClassic (ZCL)</option><option value="Zennies (ZENI)">Zennies (ZENI)</option><option value="ATLANT (ATL)">ATLANT (ATL)</option><option value="BuzzCoin (BUZZ)">BuzzCoin (BUZZ)</option><option value="Hedge (HDG)">Hedge (HDG)</option><option value="Hush (HUSH)">Hush (HUSH)</option><option value="Ethbits (ETBS)">Ethbits (ETBS)</option><option value="VIVO (VIVO)">VIVO (VIVO)</option><option value="CHIPS (CHIPS)">CHIPS (CHIPS)</option><option value="Publica (PBL)">Publica (PBL)</option><option value="Quark (QRK)">Quark (QRK)</option><option value="VeriumReserve (VRM)">VeriumReserve (VRM)</option><option value="Magi (XMG)">Magi (XMG)</option><option value="Social (SCL)">Social (SCL)</option><option value="AdShares (ADST)">AdShares (ADST)</option><option value="Zoin (ZOI)">Zoin (ZOI)</option><option value="LuckChain (BASH)">LuckChain (BASH)</option><option value="XP (XP)">XP (XP)</option><option value="FLiK (FLIK)">FLiK (FLIK)</option><option value="DNotes (NOTE)">DNotes (NOTE)</option><option value="Unity Ingot (UNY)">Unity Ingot (UNY)</option><option value="AudioCoin (ADC)">AudioCoin (ADC)</option><option value="Megacoin (MEC)">Megacoin (MEC)</option><option value="REX (REX)">REX (REX)</option><option value="Rustbits (RUSTBITS)">Rustbits (RUSTBITS)</option><option value="Paccoin (PAC)">Paccoin (PAC)</option><option value="HyperStake (HYP)">HyperStake (HYP)</option><option value="SmartBillions (SMART)">SmartBillions (SMART)</option><option value="FlypMe (FYP)">FlypMe (FYP)</option><option value="FundYourselfNow (FYN)">FundYourselfNow (FYN)</option><option value="Woodcoin (LOG)">Woodcoin (LOG)</option><option value="WorldCoin (WDC)">WorldCoin (WDC)</option><option value="BitcoinZ (BTCZ)">BitcoinZ (BTCZ)</option><option value="GCoin (GCN)">GCoin (GCN)</option><option value="Cryptonite (XCN)">Cryptonite (XCN)</option><option value="UFO Coin (UFO)">UFO Coin (UFO)</option><option value="Opus (OPT)">Opus (OPT)</option><option value="Fastcoin (FST)">Fastcoin (FST)</option><option value="Tracto (TRCT)">Tracto (TRCT)</option><option value="PiplCoin (PIPL)">PiplCoin (PIPL)</option><option value="Fantomcoin (FCN)">Fantomcoin (FCN)</option><option value="Sumokoin (SUMO)">Sumokoin (SUMO)</option><option value="EquiTrader (EQT)">EquiTrader (EQT)</option><option value="Hubii Network (HBT)">Hubii Network (HBT)</option><option value="Elementrem (ELE)">Elementrem (ELE)</option><option value="Espers (ESP)">Espers (ESP)</option><option value="Anoncoin (ANC)">Anoncoin (ANC)</option><option value="eBoost (EBST)">eBoost (EBST)</option><option value="42-coin (42)">42-coin (42)</option><option value="Altcoin (ALT)">Altcoin (ALT)</option><option value="Canada eCoin (CDN)">Canada eCoin (CDN)</option><option value="Interstellar Holdings (HOLD)">Interstellar Holdings (HOLD)</option><option value="Ellaism (ELLA)">Ellaism (ELLA)</option><option value="DraftCoin (DFT)">DraftCoin (DFT)</option><option value="Intelligent Trading Tech (ITT)">Intelligent Trading Tech (ITT)</option><option value="Crypto Bullion (CBX)">Crypto Bullion (CBX)</option><option value="AltCommunity Coin (ALTCOM)">AltCommunity Coin (ALTCOM)</option><option value="Crystal Clear Token (CCT)">Crystal Clear Token (CCT)</option><option value="KuCoin (KCS)">KuCoin (KCS)</option><option value="Rebellious (REBL)">Rebellious (REBL)</option><option value="Nuls (NULS)">Nuls (NULS)</option><option value="Upfiring (UFR)">Upfiring (UFR)</option><option value="ELTCOIN (ELTCOIN)">ELTCOIN (ELTCOIN)</option><option value="Everus (EVR)">Everus (EVR)</option><option value="Senderon (SDRN)">Senderon (SDRN)</option><option value="ASH (QASH)">ASH (QASH)</option><option value="Payfair (PFR)">Payfair (PFR)</option><option value="AdCoin (ACC)">AdCoin (ACC)</option><option value="BlakeStar (BLAS)">BlakeStar (BLAS)</option><option value="Oyster Pearl (PRL)">Oyster Pearl (PRL)</option><option value="LockChain (LOC)">LockChain (LOC)</option><option value="MediBond (MEDI)">MediBond (MEDI)</option><option value="CampusCoin (CMPCO)">CampusCoin (CMPCO)</option><option value="MonacoCoin (XMCC)">MonacoCoin (XMCC)</option><option value="PoSToken (POS)">PoSToken (POS)</option><option value="Kittehcoin (MEOW)">Kittehcoin (MEOW)</option><option value="Octanox (OTX)">Octanox (OTX)</option></select>


                        <select id="form_categories" name="form[categories][]" class="selectpicker btn-home" title="Categories - All" data-width="160" rows="4" tabindex="4" multiple="multiple"><option value="0" selected="selected">Release</option><option value="1">Rebranding</option><option value="2">Coin Supply</option><option value="3">Exchange</option><option value="4">Conference</option><option value="5">Community Event</option><option value="6">Other</option></select>


                        <select id="form_sort_by" name="form[sort_by]" class="selectpicker btn-home" data-width="fit" title="Sort by" tabindex="5"><option value=""></option><option value="created_desc">Last added</option><option value="hot_events">Hot events</option></select>

                        <button type="submit" id="form_submit" name="form[submit]" class="btn btn-s btn-d btn-round btn-filter btn-home" tabindex="6">Search</button>

                                                    <button type="submit" id="form_reset" name="form[reset]" class="btn btn-g btn-round btn-filter btn-home" tabindex="7">Reset</button>


    </form>
                    </div>
                </div>
            </div>
            <div class="text-right report-event">
                <a href="mailto:contact@coinmarketcal.com?subject=Report/Edit Event&body=Which event?%0D%0A%0D%0ADate:%0D%0ACoin:%0D%0ATitle:%0D%0A%0D%0AYour message:">Report/Edit Event</a>
            </div>
            <div class="row multi-columns-row">
                                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>12 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1160" data-date="12 December 2017" data-coin="Stellar Lumens (XLM)"
                       data-title="Satoshi Pay launch"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Stellar Lumens (XLM)</strong></h5>
        <h5>Satoshi Pay launch
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1160">
            <p class="added-date">[Added 20 November 2017]</p>
            <p class="description">
                To celebrate our launch we will organise events on 7 December in Berlin and 12 December in London.
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/9441ed18798c54a402f898770ae1b722.jpeg" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://medium.com/@SatoshiPay/satoshipay-partners-with-stellar-org-4288ae0baa72"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(812 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="89" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1160"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1160"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward the Contributor<br/>BTC: 3FzCS9Y7LyB2JZ7AYu9EoPqQ1p6Go7L87k</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>12 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1875" data-date="12 December 2017" data-coin="AirSwap (AST)"
                       data-title="Open Beta"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>AirSwap (AST)</strong></h5>
        <h5>Open Beta
                    </h5>
        <div class="content-box-info" id="box-1875">
            <p class="added-date">[Added 04 December 2017]</p>
            <p class="description">
                &quot;Open beta will be on December 12 and likely will last a week or so.&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/5a258917718f1.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://www.reddit.com/r/AirSwap/comments/7graco/airswap_ama_is_here_december_4th/"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(71 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="58" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1875"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1875"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward & Follow <a target="_blank" href="https://twitter.com/@CryptoM1KE">@CryptoM1KE</a><br/>BTC: 14vTitQ3hcaFmLdSvmD97nCv34345K1aS4</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>13 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1427" data-date="13 December 2017" data-coin="Waves (WAVES)"
                       data-title="Presentation New Client"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Waves (WAVES)</strong></h5>
        <h5>Presentation New Client
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1427">
            <p class="added-date">[Added 27 November 2017]</p>
            <p class="description">
                &quot;Presentation of the new Waves client will take place in Amsterdam, December 13&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/3ced454ae8ad125ad736d9e2749266b4.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://twitter.com/sasha35625/status/935091273278590976"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(530 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="96" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1427"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1427"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward the Contributor<br/>BTC: 114zjEb2C5H9FrXZZYJ2yygE8hoa6m3yVZ</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>13 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="2537" data-date="13 December 2017" data-coin="TrueFlip (TFL)"
                       data-title="Website Beta"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>TrueFlip (TFL)</strong></h5>
        <h5>Website Beta
                    </h5>
        <div class="content-box-info" id="box-2537">
            <p class="added-date">[Added 12 December 2017]</p>
            <p class="description">
                &quot;tomorrow we are opening beta testing of a new site&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/b7552ea13b668f6447061611477d552d.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(1 vote)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="100" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="2537"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="2537"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip"><br/>coinmarketcal.com</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>14 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1625" data-date="14 December 2017" data-coin="WeTrust (TRST)"
                       data-title="Public Tesnet Launch"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>WeTrust (TRST)</strong></h5>
        <h5>Public Tesnet Launch
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1625">
            <p class="added-date">[Added 01 December 2017]</p>
            <p class="description">
                &quot;the TLC codebase is looking good for a public testnet launch on December 14 (code freeze on December 11)&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/5a2a89de283c5.PNG" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://blog.wetrust.io/wetrust-community-update-december-7-2017-af305354f1c1"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(180 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="90" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1625"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1625"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Follow the Contributor<br/><a target="_blank" href="https://twitter.com/@crypt0pr0phet">@crypt0pr0phet</a></p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1087" data-date="15 December 2017" data-coin="ClearPoll (POLL)"
                       data-title="Alpha Testing Commences"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>ClearPoll (POLL)</strong></h5>
        <h5>Alpha Testing Commences
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1087">
            <p class="added-date">[Added 18 November 2017]</p>
            <p class="description">
                Release of the ClearPoll App Alpha. This is a huge step in the process. All alpha testers welcome, sign up through our website.
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/5d1eaa1db87e6b18abad3ae47e64260e.jpeg" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://www.clearpoll.io/updated-development-roadmap-and-new-launch-date/"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(222 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="95" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1087"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1087"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Follow the Contributor<br/><a target="_blank" href="https://twitter.com/@voteclearpoll">@voteclearpoll</a></p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1546" data-date="15 December 2017" data-coin="iXledger (IXT)"
                       data-title="MVP release"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>iXledger (IXT)</strong></h5>
        <h5>MVP release
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1546">
            <p class="added-date">[Added 30 November 2017]</p>
            <p class="description">
                No additional info            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/39e523d43c6520b07bc8afc2380b4203.jpeg" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://t.me/iXledger/17876"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(199 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="96" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1546"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1546"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward the Contributor<br/>BTC: 3GyD7m5FpPUeMB8GRiiESzQVxtELyVFGTX</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1278" data-date="15 December 2017" data-coin="Walton (WTC)"
                       data-title="Open Beta"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Walton (WTC)</strong></h5>
        <h5>Open Beta
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1278">
            <p class="added-date">[Added 23 November 2017]</p>
            <p class="description">
                Waltonchain will release the beta of its blockchain in early december.
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/5a225f423c9ea.PNG" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(164 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="91" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1278"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1278"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward & Follow <a target="_blank" href="https://twitter.com/@ASiargkas">@ASiargkas</a><br/>BTC: 1PN3iC8xnx2MVAGcoQc2yN6Rc5zT4BSp8L</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="2489" data-date="15 December 2017" data-coin="Pura (PURA)"
                       data-title="New Wallet"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Pura (PURA)</strong></h5>
        <h5>New Wallet
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-2489">
            <p class="added-date">[Added 11 December 2017]</p>
            <p class="description">
                New Wallet - Win / Linux - No Fork - Auto-updating
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/ae4b07b567de5faa390991878e4eacf9.jpeg" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://youtu.be/YwiSxlwHwP0?t=7m15s"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(131 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="98" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="2489"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="2489"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward & Follow <a target="_blank" href="https://twitter.com/@TomEliasYPR">@TomEliasYPR</a><br/>BTC: 1Ds6BQMEGncQfqqQ3HNJWtBV342jgwLzBG</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1652" data-date="15 December 2017" data-coin="Safe Exchange Coin (SAFEX)"
                       data-title="Blockchain Alpha"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Safe Exchange Coin (SAFEX)</strong></h5>
        <h5>Blockchain Alpha
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1652">
            <p class="added-date">[Added 02 December 2017]</p>
            <p class="description">
                &quot;This sounds to be on target still. Current rough target of Mid December&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/f71c13a6759c9b657520dd95b62c2133.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://safexnews.net/safex-presentation-slides-crypto-educational-tour-2017/"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(144 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="91" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1652"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1652"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip"><br/>coinmarketcal.com</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1776" data-date="15 December 2017" data-coin="NeosCoin (NEOS)"
                       data-title="Website Launch"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>NeosCoin (NEOS)</strong></h5>
        <h5>Website Launch
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1776">
            <p class="added-date">[Added 03 December 2017]</p>
            <p class="description">
                New website launch with V3 beta release
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/23d3b307d8aeb7fed8dd82a101dc2cae.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="http://www.getneos.com/#"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(93 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="89" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1776"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1776"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip"><br/>coinmarketcal.com</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="2037" data-date="15 December 2017" data-coin="EverGreenCoin (EGC)"
                       data-title="2018 Roadmap"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>EverGreenCoin (EGC)</strong></h5>
        <h5>2018 Roadmap
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-2037">
            <p class="added-date">[Added 06 December 2017]</p>
            <p class="description">
                &quot;2018 roadmap -  eta: mid December.&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/01e874a1d95324587680a795567237fe.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://bitcointalk.org/index.php?topic=2057319.msg25328852#msg25328852"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(87 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="91" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="2037"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="2037"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward & Follow <a target="_blank" href="https://twitter.com/@BedrovaFotkina">@BedrovaFotkina</a><br/>BTC: 1MvsjkkwXYSPmA1NvwqdyVgPJJWB2WcSTy</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>By 15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1774" data-date="15 December 2017" data-coin="NeosCoin (NEOS)"
                       data-title="V3 Beta Release"><i class="fa fa-clock-o"
                                                            aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>NeosCoin (NEOS)</strong></h5>
        <h5>V3 Beta Release
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1774">
            <p class="added-date">[Added 03 December 2017]</p>
            <p class="description">
                Release of Neos V3 (decentralized web platform) early December.
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/ce7b2b4853bb918eb2900e39c08df12a.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://www.reddit.com/r/NeosCoin/comments/7gtpg6/v3_beta_testing_quality_assurance/"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(86 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="86" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1774"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1774"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip"><br/>coinmarketcal.com</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="1351" data-date="15 December 2017" data-coin="Pesetacoin (PTC)"
                       data-title="Mobile wallets"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Pesetacoin (PTC)</strong></h5>
        <h5>Mobile wallets
                            <span><i class="glyphicon glyphicon-fire" aria-hidden="true" style="color:#E38C2D"></i></span>
                    </h5>
        <div class="content-box-info" id="box-1351">
            <p class="added-date">[Added 26 November 2017]</p>
            <p class="description">
                PTC will release mobile wallets for iOS and Android
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/979aa22d2c608c4244215ad07cd91267.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="http://pesetacoin.info/index_en.html"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(73 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="86" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="1351"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="1351"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward the Contributor<br/>BTC: 1NFWyn673ndgVXAuKm4KTUsab6GXWC9SJE</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="2440" data-date="15 December 2017" data-coin="Hive (HVN)"
                       data-title="Business Plan &amp; Roadmap"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>Hive (HVN)</strong></h5>
        <h5>Business Plan &amp; Roadmap
                    </h5>
        <div class="content-box-info" id="box-2440">
            <p class="added-date">[Added 11 December 2017]</p>
            <p class="description">
                &quot;We have a roadmap included in the business plan, which is to be released 15 December&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/59d5588ea503ccf50cf465590d764ea2.jpeg" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(25 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="92" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="2440"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="2440"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip"><br/>coinmarketcal.com</p>
                        </div>
</article>
                                    <article class="col-lg-3 col-md-4 col-sm-6 col-xs-12 content-box">
    <div class="content-box-general">
                    <h5><strong>15 December 2017 </strong>
                                    <a class="reminder" href="#alertReminder" data-toggle="modal" data-target="#alertReminder" data-idevent="2498" data-date="15 December 2017" data-coin="EncrypGen (DNA)"
                       data-title="Online Storefront Opening"><i class="fa fa-clock-o" aria-hidden="true"></i></a>
                            </h5>
                <h5><strong>EncrypGen (DNA)</strong></h5>
        <h5>Online Storefront Opening
                    </h5>
        <div class="content-box-info" id="box-2498">
            <p class="added-date">[Added 11 December 2017]</p>
            <p class="description">
                + &quot;Announcement of the Preferred Vendor for genetic testing&quot;
                            </p>
            <a class="btn btn-w btn-xs btn-round" href="/images/proof/143af6a29b2102b2ccf416895f5fb635.png" data-featherlight="image"><i class="fa fa-picture-o" aria-hidden="true"></i> Proof</a>
                            <a class="btn btn-w btn-xs btn-round" target="_blank" href="https://twitter.com/Encrypted_Genes/status/940310222396121091"><i class="fa fa-external-link" aria-hidden="true"></i> Source</a>

            <hr class="hr-content">
            <p style="margin-bottom: 15px;">Validation <span class="votes">(23 votes)</span></p>
            <div class="progress">
                <div class="progress-bar pb-dark" style="" aria-valuenow="87" role="progressbar" aria-valuemin="0" aria-valuemax="100"><span class="font-alt percent-value"></span></div>
            </div>
            <div class="vote-button-wrapper">

                                            <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="1" data-eventid="2498"><i class="fa fa-check" aria-hidden="true"></i> REAL </a>
                        <a href="" class="btn btn-g btn-xs btn-round btn-content vote-button" data-votevalue="0" data-eventid="2498"><i class="fa fa-times" aria-hidden="true"></i> FAKE </a>

            </div>
        </div>
                                    <p class="tip">Reward & Follow <a target="_blank" href="https://twitter.com/@ojibweghost">@ojibweghost</a><br/>BTC: 1CBLtzpgT8R2QuApbSFDA3JxcgYAyp6ugV</p>
                        </div>
</article>
                            </div>
            <div class="row" style="padding-right: 15px;">
                <nav aria-label="pagination" class="pagination-wrapper pagination">
                                    <a class="active" href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=1">1</a>
    <a  href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=2">2</a>
    <a  href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=3">3</a>
    <a  href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=4">4</a>
    <a  href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=5">5</a>
                <a href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=2">
            <i class="fa fa-angle-right"></i>
        </a>
        <a href="/?form%5Bmonth%5D=&amp;form%5Byear%5D=&amp;form%5Bcategories%5D%5B0%5D=0&amp;form%5Bsort_by%5D=&amp;form%5Bsubmit%5D=&amp;page=9">
            <i class="fa fa-angle-double-right"></i>
        </a>

                </nav>
            </div>
            <div class="row text-center" style="margin-top: 20px;">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="intrinsic-container intrinsic-container-729-90">
                <div class="coinzilla" data-zone="3299859f35cac9fcd3" data-w="729;width:100% ; height:91" data-h="91" style="max-width: 729px; width:100%; display: inline-block;"></div>
            </div>
            </div>
</div>
        </div>
    </section>
        <hr class="divider-w">
        <section class="module-extra-small">
            <div class="container">
                <div class="row">
                    <div class="col-sm-6 col-sm-offset-3">
                        <h5 class="font-alt module-subtitle" style="margin-bottom: 30px">They support the project</h5>
                    </div>
                </div>
                <div class="row">
                    <div class="owl-carousel text-center" data-items="6" data-pagination="false" data-navigation="false">
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/CryptoGat?coinmarketcal"><img src="/tweetos/9WnjDC0L_400x400.jpg" alt="@CryptoGat"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/CryptoGat?coinmarketcal">@CryptoGat</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/flyingheadofbtc?coinmarketcal"><img src="/tweetos/rIpyHkCF_400x400.jpg" alt="@flyingheadofbtc"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/flyingheadofbtc?coinmarketcal">@flyingheadofbtc</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/daytradernik?coinmarketcal"><img src="/tweetos/i1WGoUWT_400x400.jpg" alt="@daytradernik"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/daytradernik?coinmarketcal">@daytradernik</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/Coinerium?coinmarketcal"><img src="/tweetos/sF4AfIoV_400x400.jpg" alt="@Coinerium"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/Coinerium?coinmarketcal">@Coinerium</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/CryptoTutor?coinmarketcal"><img src="/tweetos/oJD_iu-Z_400x400.jpg" alt="@CryptoTutor"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/CryptoTutor?coinmarketcal">@CryptoTutor</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://discordapp.com/invite/Z3Jnh7t?coinmarketcal"><img src="/tweetos/SupErIDFaiTAlaMaIn31_400x400.jpg" alt="Les Mineurs Français"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://discordapp.com/invite/Z3Jnh7t?coinmarketcal">Les Mineurs Français</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="http://www.cryptomining-blog.com/?coinmarketcal"><img src="/tweetos/5k062aOf_400x400.png" alt="Crypto Mining Blog"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="http://www.cryptomining-blog.com/?coinmarketcal">Crypto Mining Blog</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/CryptOrca?coinmarketcal"><img src="/tweetos/ONZT-s6D_400x400.jpg" alt="@CryptOrca"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/CryptOrca?coinmarketcal">@CryptOrca</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/loomdart?coinmarketcal"><img src="/tweetos/zm7gVj-e_400x400.jpg" alt="@loomdart"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/loomdart?coinmarketcal">@loomdart</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/Coin_Shark?coinmarketcal"><img src="/tweetos/RUcyTawi_400x400.jpg" alt="@Coin_Shark"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/Coin_Shark?coinmarketcal">@Coin_Shark</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://cryptoast.fr/?coinmarketcal"><img src="/tweetos/x-K1TAL9_400x400.jpg" alt="Cryptoast"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://cryptoast.fr/?coinmarketcal">Cryptoast</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/bonzocorleonee?coinmarketcal"><img src="/tweetos/s5fT8Hay_400x400.jpg" alt="@bonzocorleonee"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/bonzocorleonee?coinmarketcal">@bonzocorleonee</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/crypto_rand?coinmarketcal"><img src="/tweetos/vqflDek9_400x400.jpg" alt="@crypto_rand"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/crypto_rand?coinmarketcal">@crypto_rand</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/LaMaisonDuBTC?coinmarketcal"><img src="/tweetos/BvMkCnGz_400x400.png" alt="@LaMaisonDuBTC"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/LaMaisonDuBTC?coinmarketcal">@LaMaisonDuBTC</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/LegendOfCrypto?coinmarketcal"><img src="/tweetos/-JFbM1q3_400x400.jpg" alt="@LegendOfCrypto"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/LegendOfCrypto?coinmarketcal">@LegendOfCrypto</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/cryptonator1337?coinmarketcal"><img src="/tweetos/9Js1Pwwk_400x400.jpg" alt="@cryptonator1337"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/cryptonator1337?coinmarketcal">@cryptonator1337</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/Cryptonoobie?coinmarketcal"><img src="/tweetos/aZApSMqr_400x400.jpg" alt="@Cryptonoobie"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/Cryptonoobie?coinmarketcal">@Cryptonoobie</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/CRYPTOBANGer?coinmarketcal"><img src="/tweetos/QiWg9tjb_400x400.jpg" alt="@CRYPTOBANGer"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/CRYPTOBANGer?coinmarketcal">@CRYPTOBANGer</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/BaleineFR?coinmarketcal"><img src="/tweetos/UbblgQXB_400x400.jpg" alt="@BaleineFR"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/BaleineFR?coinmarketcal">@BaleineFR</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://bitcoinwarrior.net/?coinmarketcal"><img src="/tweetos/17jpBpWm_400x400.jpg" alt="Bitcoin Warrior"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://bitcoinwarrior.net/?coinmarketcal">Bitcoin Warrior</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://theicodigest.com/blog/?coinmarketcal"><img src="/tweetos/SupErIDFaiTAlaMaIn312_400x400.jpg" alt="The ICO Digest"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://theicodigest.com/blog/?coinmarketcal">The ICO Digest</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/maguraaa?coinmarketcal"><img src="/tweetos/HOde6R7B_400x400.jpg" alt="@maguraaa"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/maguraaa?coinmarketcal">@maguraaa</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://bitconseil.fr/?coinmarketcal"><img src="/tweetos/bXjpZveb_400x400.jpg" alt="BitConseil"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://bitconseil.fr/?coinmarketcal">BitConseil</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/thecryptopher?coinmarketcal"><img src="/tweetos/TD3xWTAf_400x400.jpg" alt="@thecryptopher"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/thecryptopher?coinmarketcal">@thecryptopher</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/BenjaminBitcoin?coinmarketcal"><img src="/tweetos/xpFrxcz4_400x400.jpg" alt="@BenjaminBitcoin"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/BenjaminBitcoin?coinmarketcal">@BenjaminBitcoin</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://journalducoin.com/?coinmarketcal"><img src="/tweetos/RzhaX5QP_400x400.jpg" alt="Journal du Coin"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://journalducoin.com/?coinmarketcal">Journal du Coin</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/ZeusZissou?coinmarketcal"><img src="/tweetos/XYJ4akk3_400x400.jpg" alt="@ZeusZissou"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/ZeusZissou?coinmarketcal">@ZeusZissou</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/pterion2910?coinmarketcal"><img src="/tweetos/AwTrsSf2_400x400.jpg" alt="@pterion2910"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/pterion2910?coinmarketcal">@pterion2910</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/crypto_mountain?coinmarketcal"><img src="/tweetos/ZA9gRrq7_400x400.jpg" alt="@crypto_mountain"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/crypto_mountain?coinmarketcal">@crypto_mountain</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://www.youtube.com/channel/UCCatR7nWbYrkVXdxXb4cGXw?coinmarketcal"><img src="/tweetos/datadash.jpg" alt="DataDash"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://www.youtube.com/channel/UCCatR7nWbYrkVXdxXb4cGXw?coinmarketcal">DataDash</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/needacoin?coinmarketcal"><img src="/tweetos/0ygNajm8_400x400.jpg" alt="@needacoin"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/needacoin?coinmarketcal">@needacoin</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/jackfru1t?coinmarketcal"><img src="/tweetos/n5AXaHBu_400x400.jpg" alt="@jackfru1t"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/jackfru1t?coinmarketcal">@jackfru1t</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/Crypto_God?coinmarketcal"><img src="/tweetos/0cVJ3DlV_400x400.jpg" alt="@Crypto_God"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/Crypto_God?coinmarketcal">@Crypto_God</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/petersinguili?coinmarketcal"><img src="/tweetos/65535ea859717ec2843f56fc397a885b_400x400.jpeg" alt="@petersinguili"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/petersinguili?coinmarketcal">@petersinguili</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://bitcoingarden.org/?coinmarketcal"><img src="/tweetos/A8omxQnZ_400x400.jpeg" alt="Bitcoin Garden"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://bitcoingarden.org/?coinmarketcal">Bitcoin Garden</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/powerhasheur?coinmarketcal"><img src="/tweetos/hasheur.jpg" alt="@PowerHasheur"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/powerhasheur?coinmarketcal">@PowerHasheur</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/Crypto_Twitt_r?coinmarketcal"><img src="/tweetos/uvWrx288_400x400.jpg" alt="@Crypto_Twitt_r"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/Crypto_Twitt_r?coinmarketcal">@Crypto_Twitt_r</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/anambroid?coinmarketcal"><img src="/tweetos/S9j12fYh_400x400.jpg" alt="@anambroid"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/anambroid?coinmarketcal">@anambroid</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/cryptodemedici?coinmarketcal"><img src="/tweetos/qQ1h1Lhk_400x400.jpg" alt="@cryptodemedici"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/cryptodemedici?coinmarketcal">@cryptodemedici</a></h5>
                </div>
            </div>
        </div>
            <div class="owl-item">
            <div class="col-sm-12">
                <div><a target="_blank" href="https://twitter.com/onemanatatime?coinmarketcal"><img src="/tweetos/5JthaTWz_400x400.jpg" alt="@onemanatatime"/></a>
                    <h5 class="font-alt tweetos-username"><a target="_blank" href="https://twitter.com/onemanatatime?coinmarketcal">@onemanatatime</a></h5>
                </div>
            </div>
        </div>
    </div>

                </div>
            </div>
        </section>
        <section style="padding-bottom: 55px;" class="module-extra-small bg-dark">
            <div class="container">
                <div class="row">
                    <div class="col-sm-6 col-md-6 col-lg-8">
                        <div class="callout-text font-alt">
                            <p style="margin-bottom: 0px;">© 2017 CoinMarketCal | <a target="_blank" href="http://www.twitter.com/coinmarketcal"><i class="fa fa-twitter" aria-hidden="true"></i> Twitter</a></p>
                        </div>
                    </div>
                    <div class="col-sm-6 col-md-6 col-lg-4">
                        <div class="callout-text font-alt-tip">
                            <p style="margin-bottom: 0px;">Contact: anthony@coinmarketcal.com</p>
                            <p style="margin-bottom: 0px;">BTC: 1BSh6u66HeatoLcP6sjn8cBKf1BqGsvy2Z</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
    <div class="scroll-up"><a href="#totop"><i class="fa fa-angle-double-up"></i></a></div>
</main>

<script type="text/javascript" src="/js/52de33f.js"></script>

<script src="/lib/datepicker/datepicker.js"></script>
<script src="/lib/datepicker/datepicker.en.js"></script>

<script async src="https://www.googletagmanager.com/gtag/js?id=UA-107239275-1"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments)
    };
    gtag('js', new Date());

    gtag('config', 'UA-107239275-1');
</script>

<script async src="//apps.cointraffic.io/js/?wkey=AQjeL1"></script>
<script async src="https://serve.czilladx.com/serve/jslib/fb.js"></script>
<script src="//m.servedby-buysellads.com/monetization.js" type="text/javascript"></script>
<script>
    (function () {
        if (typeof _bsa !== 'undefined' && _bsa) {
            _bsa.init('fancybar', 'CKYDV2QM', 'placement:coinmarketcal');
        }
    })();
</script>

    <script>
        $('.vote-button').click(function () {
            var eventId = $(this).data("eventid");
            var voteValue = $(this).data("votevalue");
            $.ajax({
                url: '/vote',
                type: 'POST',
                data: {'id': eventId, 'up': voteValue},
                dataType: 'json',
                success: function (data) {
                    var $eventHTML = $("#box-" + eventId);
                    if (data.error) {
                        $eventHTML.find(".vote-button-wrapper").html('<a class="btn btn-w btn-xs btn-round btn-content">' + data.error + '</a>')
                    }
                    else {
                        var voteLabel = (data.count > 0) ? "votes" : "vote";
                        $eventHTML.find(".progress-bar").width(data.percent + "%");
                        $eventHTML.find(".percent-value").html(data.percent);
                        $eventHTML.find(".votes").html("(" + data.count + " " + voteLabel + ")");
                        $eventHTML.find(".vote-button-wrapper").html('<a class="btn btn-w btn-xs btn-round btn-content">Thanks for your help!</a>')
                    }
                }
            });
            return false;
        });

        $('#alertReminder').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget);
            var recipient = button.data('idevent');
            var coin = button.data('coin');
            var date = button.data('date');
            var title = button.data('title');
            var modal = $(this);
            modal.find('#form_event_id').val(recipient);
            modal.find('#remindereventcoin').html(coin);
            modal.find('#remindereventdate').html(date);
            modal.find('#remindereventtitle').html(title);
        })
    </script>

    <script type="text/javascript">
        var recaptchaAlert;
        var recaptchaReminder;
        var onloadCallback = function () {
            recaptchaAlert = grecaptcha.render('recaptchaAlert', {
                'sitekey': '6LdNBjIUAAAAAM5JR_gK7-lMz0hRHYBXAuYilQVp',
            });
            recaptchaReminder = grecaptcha.render('recaptchaReminder', {
                'sitekey': '6LdNBjIUAAAAAM5JR_gK7-lMz0hRHYBXAuYilQVp'
            });
        };
    </script>

<script src="https://www.google.com/recaptcha/api.js?onload=onloadCallback&render=explicit" async defer></script>

</body>
</html>
"""

from bs4 import BeautifulSoup
import os
import sqlite3
import urllib.request

class DatabaseWorker:

    def __new__(cls):
        """ Signleton Pattern. Checks for existing instance before creating a
        new instance """
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseWorker, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        sqlite_file = os.path.join(os.path.dirname(__file__), 'db.sqlite')
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()

        self.create_database()

    def create_database(self):
        """ Create the database if it does not already exist """

        print('Creating database if it does not already exist')
        create_table_statement = """
            CREATE TABLE
            IF NOT EXISTS events (
             id integer PRIMARY KEY,
             coin text NOT NULL,
             event_date text,
             description text,
             posted_date text,
             validation integer,
             event_type text,
             buy_low real,
             buy_avg real,
             buy_high real,
             sell_high real,
             sell_date text,
             high_btc real,
             late_sell_low real,
             late_sell_avg real,
             late_sell_high real
            );
        """
        self.c.execute(create_table_statement)

        self.conn.commit()


    def add_record(self, data):
        """ Add a new record to the database with supplied dictionary """

        if not self.already_exists_with_different_event_type(data):
            sql = 'INSERT INTO events ('

            keys = list(data)
            values = list(data.values())
            values = list(map(lambda x: "\'" + x + "\'", values))

            sql += ', '.join(keys) + ') VALUES ('
            sql += ', '.join(values) + ');'
            self.c.execute(sql)
            self.conn.commit()

    def already_exists(self, data):
        """ Check to see if record already exists in the database. This is used
        for scraping the website to see if we can stop scraping because we are
        up to date. The validity can change, so we ignore that. """
        sql = 'SELECT * FROM events WHERE '

        keys = list(data)
        values = list(data.values())

        validation_index = keys.index('validation')
        del keys[validation_index]
        del values[validation_index]

        values = list(map(lambda x: "\'" + x + "\'", values))

        where_statement = []
        for i, val in enumerate(keys):
            where_statement.append("{0} = {1}".format(keys[i], values[i]))

        sql += ' AND '.join(where_statement) + ';'

        result = self.c.execute(sql)
        rows = self.c.fetchall()

        return len(rows) > 0

    def already_exists_with_different_event_type(self, data):
        """ Check to see if record already exists in the database, but with a
        different category """

        sql = 'SELECT * FROM events WHERE '

        keys = list(data)
        values = list(data.values())

        event_type_index = keys.index('event_type')
        del keys[event_type_index]
        del values[event_type_index]

        values = list(map(lambda x: "\'" + x + "\'", values))

        where_statement = []
        for i, val in enumerate(keys):
            where_statement.append("{0} = {1}".format(keys[i], values[i]))

        sql += ' AND '.join(where_statement) + ';'

        result = self.c.execute(sql)
        rows = self.c.fetchall()

        return len(rows) > 0



    def __del__(self):
        """ Close the database when the object is destroyed """
        # TODO replace with https://en.wikibooks.org/wiki/Python_Programming/Context_Managers
        self.conn.close()



def main():
    """ Main entry point of the app """

    scrape()


def scrape():
    """ Scrapes the event data and adds it to the database """
    print('Scraping events')

    base_url = 'http://coinmarketcal.com'

    categories = {0: 'Release',
                    1: 'Rebranding',
                    2: 'Coin Supply',
                    3: 'Exchange',
                    4: 'Conference',
                    5: 'Community Event',
                    6: 'Other'}

    db = DatabaseWorker()

    for key, value in categories.items():
        print ("{0}:{1}".format(key, value))

        html_doc = urllib.request.urlopen("{0}/pastevents?form%5bcategories%5d%5b%5d={1}".format(base_url, key))
        scraper = BeautifulSoup(html_doc, 'html.parser')

        # emulate do while
        up_to_date = False
        while not up_to_date:
            for item in scraper.find_all('div', class_='content-box-general'):
                event_date = item.h5.strong.get_text()
                coin = item.h5.next_sibling.next_sibling.strong.get_text()
                description = item.h5.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
                posted_date = item.find('p', class_='added-date').get_text()
                validation = item.find('div', class_='progress-bar').get('aria-valuenow')
                data = {'event_date': event_date,
                        'coin': coin,
                        'description': description,
                        'posted_date': posted_date,
                        'validation': validation,
                        'event_type': value}
                if (db.already_exists(data)):
                    # up to date, move on to next category
                    print("{0}: up to date".format(value))
                    up_to_date = True
                    break;
                else:
                    print("{0}: adding record for {1}".format(value, coin))
                    db.add_record(data)

            next_page = scraper.find('i', class_='fa fa-angle-right')
            if (next_page):
                next_page = next_page.parent.get('href')
                html_doc = urllib.request.urlopen("{0}{1}".format(base_url, next_page))
                scraper = BeautifulSoup(html_doc, 'html.parser')
            else:
                up_to_date = True;

def get_prices():
    """ Get prices for all past events """
    # TODO

def generate_html():
    """ Generate HTML document with all the data from the database """
    # TODO

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
