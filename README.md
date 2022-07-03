# Peatio_API_DOCS
<html><head></head><body><link rel="stylesheet" type="text/css" href="vostok.css" id="_theme"><div id="_html" class="markdown-theme"><span class="octicon octicon-link"></span></a>Peatio Trade Exchange User API</h1>
<p>API for XCHFORKS Exchange.</p>
<p><strong>https://xchforks.trade/api/peatio/v2</strong>
<h3 id="security"><a class="anchor" name="security" href="#security"><span class="octicon octicon-link"></span></a>Security</h3>
<p><strong>Bearer</strong>  </p>
<table>
<thead>
<tr>
<th>apiKey</th>
<th><em>API Key</em></th>
</tr>
</thead>
<tbody><tr>
<td>Name</td>
<td>JWT</td>
</tr>
<tr>
<td>In</td>
<td>header</td>
</tr>
</tbody></table>
<h3 id="-public-maintenance-last"><a class="anchor" name="-public-maintenance-last" href="#-public-maintenance-last"><span class="octicon octicon-link"></span></a>/public/maintenance/last</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get maintenance</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get maintenance</td>
<td><a href="#maintenance">Maintenance</a></td>
</tr>
</tbody></table>
<h3 id="-public-health-ready"><a class="anchor" name="-public-health-ready" href="#-public-health-ready"><span class="octicon octicon-link"></span></a>/public/health/ready</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get application readiness status</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get application readiness status</td>
</tr>
</tbody></table>
<h3 id="-public-health-alive"><a class="anchor" name="-public-health-alive" href="#-public-health-alive"><span class="octicon octicon-link"></span></a>/public/health/alive</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get application liveness status</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get application liveness status</td>
</tr>
</tbody></table>
<h3 id="-public-version"><a class="anchor" name="-public-version" href="#-public-version"><span class="octicon octicon-link"></span></a>/public/version</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get running Peatio Trade version and build details.</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get running Peatio Trade version and build details.</td>
</tr>
</tbody></table>
<h3 id="-public-timestamp"><a class="anchor" name="-public-timestamp" href="#-public-timestamp"><span class="octicon octicon-link"></span></a>/public/timestamp</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get server current time, in seconds since Unix epoch.</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get server current time, in seconds since Unix epoch.</td>
</tr>
</tbody></table>
<h3 id="-public-member-levels"><a class="anchor" name="-public-member-levels" href="#-public-member-levels"><span class="octicon octicon-link"></span></a>/public/member-levels</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Returns hash of minimum levels and the privileges they provide.</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Returns hash of minimum levels and the privileges they provide.</td>
</tr>
</tbody></table>
<h3 id="-public-markets-market-tickers"><a class="anchor" name="-public-markets-market-tickers" href="#-public-markets-market-tickers"><span class="octicon octicon-link"></span></a>/public/markets/{market}/tickers</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get ticker of specific market.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>path</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get ticker of specific market.</td>
</tr>
</tbody></table>
<h3 id="-public-markets-tickers"><a class="anchor" name="-public-markets-tickers" href="#-public-markets-tickers"><span class="octicon octicon-link"></span></a>/public/markets/tickers</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get ticker of all markets.</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get ticker of all markets.</td>
</tr>
</tbody></table>
<h3 id="-public-markets-market-k-line"><a class="anchor" name="-public-markets-market-k-line" href="#-public-markets-market-k-line"><span class="octicon octicon-link"></span></a>/public/markets/{market}/k-line</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get OHLC(k line) of specific market.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>path</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>period</td>
<td>query</td>
<td>Time period of K line, default to 1. You can choose between 1, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>time_from</td>
<td>query</td>
<td>An integer represents the seconds elapsed since Unix epoch. If set, only k-line data after that time will be returned.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>time_to</td>
<td>query</td>
<td>An integer represents the seconds elapsed since Unix epoch. If set, only k-line data till that time will be returned.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Limit the number of returned data points default to 30. Ignored if time_from and time_to are given.</td>
<td>No</td>
<td>integer</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get OHLC(k line) of specific market.</td>
</tr>
</tbody></table>
<h3 id="-public-markets-market-depth"><a class="anchor" name="-public-markets-market-depth" href="#-public-markets-market-depth"><span class="octicon octicon-link"></span></a>/public/markets/{market}/depth</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get depth or specified market. Both asks and bids are sorted from highest price to lowest.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>path</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Limit the number of returned price levels. Default to 300.</td>
<td>No</td>
<td>integer</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get depth or specified market. Both asks and bids are sorted from highest price to lowest.</td>
</tr>
</tbody></table>
<h3 id="-public-markets-market-trades"><a class="anchor" name="-public-markets-market-trades" href="#-public-markets-market-trades"><span class="octicon octicon-link"></span></a>/public/markets/{market}/trades</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get recent trades on market, each trade is included only once. Trades are sorted in reverse creation order.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>path</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Limit the number of returned trades. Default to 100.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>page</td>
<td>query</td>
<td>Specify the page of paginated results.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>timestamp</td>
<td>query</td>
<td>An integer represents the seconds elapsed since Unix epoch.If set, only trades executed before the time will be returned.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>order_by</td>
<td>query</td>
<td>If set, returned trades will be sorted in specific order, default to 'desc'.</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get recent trades on market, each trade is included only once. Trades are sorted in reverse creation order.</td>
<td>[ <a href="#trade">Trade</a> ]</td>
</tr>
</tbody></table>
<h3 id="-public-markets-market-order-book"><a class="anchor" name="-public-markets-market-order-book" href="#-public-markets-market-order-book"><span class="octicon octicon-link"></span></a>/public/markets/{market}/order-book</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get the order book of specified market.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>path</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>asks_limit</td>
<td>query</td>
<td>Limit the number of returned sell orders. Default to 20.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>bids_limit</td>
<td>query</td>
<td>Limit the number of returned buy orders. Default to 20.</td>
<td>No</td>
<td>integer</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get the order book of specified market.</td>
<td>[ <a href="#orderbook">OrderBook</a> ]</td>
</tr>
</tbody></table>
<h3 id="-public-markets"><a class="anchor" name="-public-markets" href="#-public-markets"><span class="octicon octicon-link"></span></a>/public/markets</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get all available markets.</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get all available markets.</td>
<td>[ <a href="#market">Market</a> ]</td>
</tr>
</tbody></table>
<h3 id="-public-currencies"><a class="anchor" name="-public-currencies" href="#-public-currencies"><span class="octicon octicon-link"></span></a>/public/currencies</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get list of currencies</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>query</td>
<td>Currency type</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get list of currencies</td>
<td>[ <a href="#currency">Currency</a> ]</td>
</tr>
</tbody></table>
<h3 id="-public-currencies-id-"><a class="anchor" name="-public-currencies-id-" href="#-public-currencies-id-"><span class="octicon octicon-link"></span></a>/public/currencies/{id}</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get a currency</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>path</td>
<td>Currency code.</td>
<td>Yes</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get a currency</td>
<td><a href="#currency">Currency</a></td>
</tr>
</tbody></table>
<h3 id="-account-rewards"><a class="anchor" name="-account-rewards" href="#-account-rewards"><span class="octicon octicon-link"></span></a>/account/rewards</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>List your rewards as paginated collection.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>currency</td>
<td>query</td>
<td>Currency code.</td>
<td>No</td>
<td>string</td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Number of withdraws per page (defaults to 100, maximum is 100).</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>page</td>
<td>query</td>
<td>Page number (defaults to 1).</td>
<td>No</td>
<td>integer</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>List your rewards as paginated collection.</td>
<td>[ <a href="#reward">Reward</a> ]</td>
</tr>
</tbody></table>
<h3 id="-account-balances-currency-"><a class="anchor" name="-account-balances-currency-" href="#-account-balances-currency-"><span class="octicon octicon-link"></span></a>/account/balances/{currency}</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get user account by currency</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>currency</td>
<td>path</td>
<td>The currency code.</td>
<td>Yes</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get user account by currency</td>
<td><a href="#account">Account</a></td>
</tr>
</tbody></table>
<h3 id="-account-balances"><a class="anchor" name="-account-balances" href="#-account-balances"><span class="octicon octicon-link"></span></a>/account/balances</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get list of user accounts</p>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get list of user accounts</td>
<td>[ <a href="#account">Account</a> ]</td>
</tr>
</tbody></table>
<h3 id="-account-deposit_address-currency-"><a class="anchor" name="-account-deposit_address-currency-" href="#-account-deposit_address-currency-"><span class="octicon octicon-link"></span></a>/account/deposit_address/{currency}</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Returns deposit address for account you want to deposit to by currency. The address may be blank because address generation process is still in progress. If this case you should try again later.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>currency</td>
<td>path</td>
<td>The account you want to deposit to.</td>
<td>Yes</td>
<td>string</td>
</tr>
<tr>
<td>address_format</td>
<td>query</td>
<td>Address format legacy/cash</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Returns deposit address for account you want to deposit to by currency. The address may be blank because address generation process is still in progress. If this case you should try again later.</td>
<td><a href="#deposit">Deposit</a></td>
</tr>
</tbody></table>
<h3 id="-account-deposits-txid-"><a class="anchor" name="-account-deposits-txid-" href="#-account-deposits-txid-"><span class="octicon octicon-link"></span></a>/account/deposits/{txid}</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get details of specific deposit.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>txid</td>
<td>path</td>
<td>Deposit transaction id</td>
<td>Yes</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get details of specific deposit.</td>
<td><a href="#deposit">Deposit</a></td>
</tr>
</tbody></table>
<h3 id="-account-deposits"><a class="anchor" name="-account-deposits" href="#-account-deposits"><span class="octicon octicon-link"></span></a>/account/deposits</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get your deposits history.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>currency</td>
<td>query</td>
<td>Currency code</td>
<td>No</td>
<td>string</td>
</tr>
<tr>
<td>state</td>
<td>query</td>
<td>| No</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Number of deposits per page (defaults to 100, maximum is 100).</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>page</td>
<td>query</td>
<td>Page number (defaults to 1).</td>
<td>No</td>
<td>integer</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get your deposits history.</td>
<td>[ <a href="#deposit">Deposit</a> ]</td>
</tr>
</tbody></table>
<h3 id="-account-withdraws"><a class="anchor" name="-account-withdraws" href="#-account-withdraws"><span class="octicon octicon-link"></span></a>/account/withdraws</h3>
<h4 id="post"><a class="anchor" name="post" href="#post"><span class="octicon octicon-link"></span></a>POST</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Creates new crypto withdrawal.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>otp</td>
<td>formData</td>
<td>OTP to perform action</td>
<td>Yes</td>
<td>integer</td>
</tr>
<tr>
<td>rid</td>
<td>formData</td>
<td>Wallet address on the Blockchain.</td>
<td>Yes</td>
<td>string</td>
</tr>
<tr>
<td>currency</td>
<td>formData</td>
<td>The currency code.</td>
<td>Yes</td>
<td>string</td>
</tr>
<tr>
<td>amount</td>
<td>formData</td>
<td>The amount to withdraw.</td>
<td>Yes</td>
<td>double</td>
</tr>
<tr>
<td>note</td>
<td>formData</td>
<td>Optional metadata to be applied to the transaction. Used to tag transactions with memorable comments.</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>201</td>
<td>Creates new crypto withdrawal.</td>
</tr>
</tbody></table>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>List your withdraws as paginated collection.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>currency</td>
<td>query</td>
<td>Currency code.</td>
<td>No</td>
<td>string</td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Number of withdraws per page (defaults to 100, maximum is 100).</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>page</td>
<td>query</td>
<td>Page number (defaults to 1).</td>
<td>No</td>
<td>integer</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>List your withdraws as paginated collection.</td>
<td>[ <a href="#withdraw">Withdraw</a> ]</td>
</tr>
</tbody></table>
<h3 id="-market-trades"><a class="anchor" name="-market-trades" href="#-market-trades"><span class="octicon octicon-link"></span></a>/market/trades</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get your executed trades. Trades are sorted in reverse creation order.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>query</td>
<td>| No</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Limit the number of returned trades. Default to 100.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>page</td>
<td>query</td>
<td>Specify the page of paginated results.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>time_from</td>
<td>query</td>
<td>An integer represents the seconds elapsed since Unix epoch.If set, only trades executed after the time will be returned.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>time_to</td>
<td>query</td>
<td>An integer represents the seconds elapsed since Unix epoch.If set, only trades executed before the time will be returned.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>order_by</td>
<td>query</td>
<td>If set, returned trades will be sorted in specific order, default to 'desc'.</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get your executed trades. Trades are sorted in reverse creation order.</td>
<td>[ <a href="#trade">Trade</a> ]</td>
</tr>
</tbody></table>
<h3 id="-market-orders-cancel"><a class="anchor" name="-market-orders-cancel" href="#-market-orders-cancel"><span class="octicon octicon-link"></span></a>/market/orders/cancel</h3>
<h4 id="post"><a class="anchor" name="post" href="#post"><span class="octicon octicon-link"></span></a>POST</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Cancel all my orders.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>formData</td>
<td>| No</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>side</td>
<td>formData</td>
<td>If present, only sell orders (asks) or buy orders (bids) will be canncelled.</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>201</td>
<td>Cancel all my orders.</td>
<td><a href="#order">Order</a></td>
</tr>
</tbody></table>
<h3 id="-market-orders-id-cancel"><a class="anchor" name="-market-orders-id-cancel" href="#-market-orders-id-cancel"><span class="octicon octicon-link"></span></a>/market/orders/{id}/cancel</h3>
<h4 id="post"><a class="anchor" name="post" href="#post"><span class="octicon octicon-link"></span></a>POST</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Cancel an order.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>path</td>
<td>| Yes</td>
<td>integer</td>
<td></td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>201</td>
<td>Cancel an order.</td>
</tr>
</tbody></table>
<h3 id="-market-orders"><a class="anchor" name="-market-orders" href="#-market-orders"><span class="octicon octicon-link"></span></a>/market/orders</h3>
<h4 id="post"><a class="anchor" name="post" href="#post"><span class="octicon octicon-link"></span></a>POST</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Create a Sell/Buy order.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>formData</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>side</td>
<td>formData</td>
<td>| Yes</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>volume</td>
<td>formData</td>
<td>| Yes</td>
<td>double</td>
<td></td>
</tr>
<tr>
<td>ord_type</td>
<td>formData</td>
<td>| No</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>price</td>
<td>formData</td>
<td>| Yes</td>
<td>double</td>
<td></td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>201</td>
<td>Create a Sell/Buy order.</td>
<td><a href="#order">Order</a></td>
</tr>
</tbody></table>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get your orders, results is paginated.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>market</td>
<td>query</td>
<td>| No</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>state</td>
<td>query</td>
<td>Filter order by state.</td>
<td>No</td>
<td>string</td>
</tr>
<tr>
<td>limit</td>
<td>query</td>
<td>Limit the number of returned orders, default to 100.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>page</td>
<td>query</td>
<td>Specify the page of paginated results.</td>
<td>No</td>
<td>integer</td>
</tr>
<tr>
<td>order_by</td>
<td>query</td>
<td>If set, returned orders will be sorted in specific order, default to "desc".</td>
<td>No</td>
<td>string</td>
</tr>
<tr>
<td>ord_type</td>
<td>query</td>
<td>Filter order by ord_type.</td>
<td>No</td>
<td>string</td>
</tr>
<tr>
<td>type</td>
<td>query</td>
<td>Filter order by type.</td>
<td>No</td>
<td>string</td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get your orders, results is paginated.</td>
<td>[ <a href="#order">Order</a> ]</td>
</tr>
</tbody></table>
<h3 id="-market-orders-id-"><a class="anchor" name="-market-orders-id-" href="#-market-orders-id-"><span class="octicon octicon-link"></span></a>/market/orders/{id}</h3>
<h4 id="get"><a class="anchor" name="get" href="#get"><span class="octicon octicon-link"></span></a>GET</h4>
<h5 id="description-"><a class="anchor" name="description-" href="#description-"><span class="octicon octicon-link"></span></a>Description:</h5>
<p>Get information of specified order.</p>
<h5 id="parameters"><a class="anchor" name="parameters" href="#parameters"><span class="octicon octicon-link"></span></a>Parameters</h5>
<table>
<thead>
<tr>
<th>Name</th>
<th>Located in</th>
<th>Description</th>
<th>Required</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>path</td>
<td>| Yes</td>
<td>integer</td>
<td></td>
</tr>
</tbody></table>
<h5 id="responses"><a class="anchor" name="responses" href="#responses"><span class="octicon octicon-link"></span></a>Responses</h5>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
<th>Schema</th>
</tr>
</thead>
<tbody><tr>
<td>200</td>
<td>Get information of specified order.</td>
<td><a href="#order">Order</a></td>
</tr>
</tbody></table>
<h3 id="models"><a class="anchor" name="models" href="#models"><span class="octicon octicon-link"></span></a>Models</h3>
<h4 id="maintenance"><a class="anchor" name="maintenance" href="#maintenance"><span class="octicon octicon-link"></span></a>Maintenance</h4>
<p>Get maintenance</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>is_maintenance</td>
<td>string</td>
<td>is Maintenance</td>
<td>No</td>
</tr>
<tr>
<td>is_plan</td>
<td>string</td>
<td>is Planed</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="trade"><a class="anchor" name="trade" href="#trade"><span class="octicon octicon-link"></span></a>Trade</h4>
<p>Get your executed trades. Trades are sorted in reverse creation order.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>string</td>
<td>Trade ID.</td>
<td>No</td>
</tr>
<tr>
<td>price</td>
<td>double</td>
<td>Trade price.</td>
<td>No</td>
</tr>
<tr>
<td>volume</td>
<td>double</td>
<td>Trade volume.</td>
<td>No</td>
</tr>
<tr>
<td>funds</td>
<td>double</td>
<td>Trade funds.</td>
<td>No</td>
</tr>
<tr>
<td>market</td>
<td>string</td>
<td>Trade market id.</td>
<td>No</td>
</tr>
<tr>
<td>created_at</td>
<td>string</td>
<td>Trade create time in iso8601 format.</td>
<td>No</td>
</tr>
<tr>
<td>taker_type</td>
<td>string</td>
<td>Trade maker order type (sell or buy).</td>
<td>No</td>
</tr>
<tr>
<td>side</td>
<td>string</td>
<td>Trade side.</td>
<td>No</td>
</tr>
<tr>
<td>order_id</td>
<td>integer</td>
<td>Order id.</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="orderbook"><a class="anchor" name="orderbook" href="#orderbook"><span class="octicon octicon-link"></span></a>OrderBook</h4>
<p>Get the order book of specified market.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>asks</td>
<td>[ <a href="#order">Order</a> ]</td>
<td>Asks in orderbook</td>
<td>No</td>
</tr>
<tr>
<td>bids</td>
<td>[ <a href="#order">Order</a> ]</td>
<td>Bids in orderbook</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="order"><a class="anchor" name="order" href="#order"><span class="octicon octicon-link"></span></a>Order</h4>
<p>Get your orders, results is paginated.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>integer</td>
<td>Unique order id.</td>
<td>No</td>
</tr>
<tr>
<td>side</td>
<td>string</td>
<td>Either 'sell' or 'buy'.</td>
<td>No</td>
</tr>
<tr>
<td>ord_type</td>
<td>string</td>
<td>Type of order, either 'limit' or 'market'.</td>
<td>No</td>
</tr>
<tr>
<td>price</td>
<td>double</td>
<td>Price for each unit. e.g.If you want to sell/buy 1 btc at 3000 usd, the price is '3000.0'</td>
<td>No</td>
</tr>
<tr>
<td>avg_price</td>
<td>double</td>
<td>Average execution price, average of price in trades.</td>
<td>No</td>
</tr>
<tr>
<td>state</td>
<td>string</td>
<td>One of 'wait', 'done', or 'cancel'.An order in 'wait' is an active order, waiting fulfillment;a 'done' order is an order fulfilled;'cancel' means the order has been canceled.</td>
<td>No</td>
</tr>
<tr>
<td>market</td>
<td>string</td>
<td>The market in which the order is placed, e.g. 'btcusd'.All available markets can be found at /api/v2/markets.</td>
<td>No</td>
</tr>
<tr>
<td>created_at</td>
<td>string</td>
<td>Order create time in iso8601 format.</td>
<td>No</td>
</tr>
<tr>
<td>updated_at</td>
<td>string</td>
<td>Order updated time in iso8601 format.</td>
<td>No</td>
</tr>
<tr>
<td>origin_volume</td>
<td>double</td>
<td>The amount user want to sell/buy.An order could be partially executed,e.g. an order sell 5 btc can be matched with a buy 3 btc order,left 2 btc to be sold; in this case the order's volume would be '5.0',its remaining_volume would be '2.0', its executed volume is '3.0'.</td>
<td>No</td>
</tr>
<tr>
<td>remaining_volume</td>
<td>double</td>
<td>The remaining volume, see 'volume'.</td>
<td>No</td>
</tr>
<tr>
<td>executed_volume</td>
<td>double</td>
<td>The executed volume, see 'volume'.</td>
<td>No</td>
</tr>
<tr>
<td>trades_count</td>
<td>integer</td>
<td>Count of trades.</td>
<td>No</td>
</tr>
<tr>
<td>trades</td>
<td>[ <a href="#trade">Trade</a> ]</td>
<td>Trades wiht this order.</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="market"><a class="anchor" name="market" href="#market"><span class="octicon octicon-link"></span></a>Market</h4>
<p>Get all available markets.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>string</td>
<td>Unique market id. It's always in the form of xxxyyy,where xxx is the base currency code, yyy is the quotecurrency code, e.g. 'btcusd'. All available markets canbe found at /api/v2/markets.</td>
<td>No</td>
</tr>
<tr>
<td>name</td>
<td>string</td>
<td>Market name.</td>
<td>No</td>
</tr>
<tr>
<td>ask_unit</td>
<td>string</td>
<td>Market ask unit.</td>
<td>No</td>
</tr>
<tr>
<td>bid_unit</td>
<td>string</td>
<td>Market bid unit.</td>
<td>No</td>
</tr>
<tr>
<td>ask_fee</td>
<td>double</td>
<td>Market ask fee.</td>
<td>No</td>
</tr>
<tr>
<td>bid_fee</td>
<td>double</td>
<td>Market bid fee.</td>
<td>No</td>
</tr>
<tr>
<td>min_ask_price</td>
<td>double</td>
<td>Max ask order price.</td>
<td>No</td>
</tr>
<tr>
<td>max_bid_price</td>
<td>double</td>
<td>Max bid order price.</td>
<td>No</td>
</tr>
<tr>
<td>min_ask_amount</td>
<td>double</td>
<td>Min ask order amount.</td>
<td>No</td>
</tr>
<tr>
<td>min_bid_amount</td>
<td>double</td>
<td>Min bid order amount.</td>
<td>No</td>
</tr>
<tr>
<td>ask_precision</td>
<td>double</td>
<td>Precision for ask order.</td>
<td>No</td>
</tr>
<tr>
<td>bid_precision</td>
<td>double</td>
<td>Precision for bid order.</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="currency"><a class="anchor" name="currency" href="#currency"><span class="octicon octicon-link"></span></a>Currency</h4>
<p>Get a currency</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>string</td>
<td>Currency code.</td>
<td>No</td>
</tr>
<tr>
<td>name</td>
<td>string</td>
<td>Currency name</td>
<td>No</td>
</tr>
<tr>
<td>symbol</td>
<td>string</td>
<td>Currency symbol</td>
<td>No</td>
</tr>
<tr>
<td>explorer_transaction</td>
<td>string</td>
<td>Currency transaction exprorer url template</td>
<td>No</td>
</tr>
<tr>
<td>explorer_address</td>
<td>string</td>
<td>Currency address exprorer url template</td>
<td>No</td>
</tr>
<tr>
<td>type</td>
<td>string</td>
<td>Currency type</td>
<td>No</td>
</tr>
<tr>
<td>deposit_fee</td>
<td>string</td>
<td>Currency deposit fee</td>
<td>No</td>
</tr>
<tr>
<td>min_deposit_amount</td>
<td>string</td>
<td>Minimal deposit amount</td>
<td>No</td>
</tr>
<tr>
<td>withdraw_fee</td>
<td>string</td>
<td>Currency withdraw fee</td>
<td>No</td>
</tr>
<tr>
<td>min_withdraw_amount</td>
<td>string</td>
<td>Minimal withdraw amount</td>
<td>No</td>
</tr>
<tr>
<td>withdraw_limit_24h</td>
<td>string</td>
<td>Currency 24h withdraw limit</td>
<td>No</td>
</tr>
<tr>
<td>withdraw_limit_72h</td>
<td>string</td>
<td>Currency 72h withdraw limit</td>
<td>No</td>
</tr>
<tr>
<td>base_factor</td>
<td>string</td>
<td>Currency base factor</td>
<td>No</td>
</tr>
<tr>
<td>precision</td>
<td>string</td>
<td>Currency precision</td>
<td>No</td>
</tr>
<tr>
<td>icon_url</td>
<td>string</td>
<td>Currency icon</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="reward"><a class="anchor" name="reward" href="#reward"><span class="octicon octicon-link"></span></a>Reward</h4>
<p>List your rewards as paginated collection.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>integer</td>
<td>The withdrawal id.</td>
<td>No</td>
</tr>
<tr>
<td>currency</td>
<td>string</td>
<td>The currency code.</td>
<td>No</td>
</tr>
<tr>
<td>price</td>
<td>double</td>
<td>The reward amount</td>
<td>No</td>
</tr>
<tr>
<td>reward_type</td>
<td>string</td>
<td>The reward type</td>
<td>No</td>
</tr>
<tr>
<td>amount</td>
<td>double</td>
<td>The reward amount</td>
<td>No</td>
</tr>
<tr>
<td>usd_amount</td>
<td>double</td>
<td>The reward in amount.</td>
<td>No</td>
</tr>
<tr>
<td>created_at</td>
<td>string</td>
<td>The datetimes for the reward.</td>
<td>No</td>
</tr>
<tr>
<td>updated_at</td>
<td>string</td>
<td>The datetimes for the reward.</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="account"><a class="anchor" name="account" href="#account"><span class="octicon octicon-link"></span></a>Account</h4>
<p>Get list of user accounts</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>currency</td>
<td>string</td>
<td>Currency code.</td>
<td>No</td>
</tr>
<tr>
<td>balance</td>
<td>double</td>
<td>Account balance.</td>
<td>No</td>
</tr>
<tr>
<td>locked</td>
<td>double</td>
<td>Account locked funds.</td>
<td>No</td>
</tr>
<tr>
<td>total</td>
<td>double</td>
<td>Currency code.</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="deposit"><a class="anchor" name="deposit" href="#deposit"><span class="octicon octicon-link"></span></a>Deposit</h4>
<p>Get your deposits history.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>integer</td>
<td>Unique deposit id.</td>
<td>No</td>
</tr>
<tr>
<td>currency</td>
<td>string</td>
<td>Deposit currency id.</td>
<td>No</td>
</tr>
<tr>
<td>amount</td>
<td>double</td>
<td>Deposit amount.</td>
<td>No</td>
</tr>
<tr>
<td>fee</td>
<td>double</td>
<td>Deposit fee.</td>
<td>No</td>
</tr>
<tr>
<td>txid</td>
<td>string</td>
<td>Deposit transaction id.</td>
<td>No</td>
</tr>
<tr>
<td>confirmations</td>
<td>integer</td>
<td>Number of deposit confirmations.</td>
<td>No</td>
</tr>
<tr>
<td>state</td>
<td>string</td>
<td>Deposit state.</td>
<td>No</td>
</tr>
<tr>
<td>created_at</td>
<td>string</td>
<td>The datetime when deposit was created.</td>
<td>No</td>
</tr>
<tr>
<td>completed_at</td>
<td>string</td>
<td>The datetime when deposit was completed..</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="withdraw"><a class="anchor" name="withdraw" href="#withdraw"><span class="octicon octicon-link"></span></a>Withdraw</h4>
<p>List your withdraws as paginated collection.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>id</td>
<td>integer</td>
<td>The withdrawal id.</td>
<td>No</td>
</tr>
<tr>
<td>currency</td>
<td>string</td>
<td>The currency code.</td>
<td>No</td>
</tr>
<tr>
<td>type</td>
<td>string</td>
<td>The withdrawal type</td>
<td>No</td>
</tr>
<tr>
<td>amount</td>
<td>string</td>
<td>The withdrawal amount</td>
<td>No</td>
</tr>
<tr>
<td>fee</td>
<td>double</td>
<td>The exchange fee.</td>
<td>No</td>
</tr>
<tr>
<td>blockchain_txid</td>
<td>string</td>
<td>The withdrawal transaction id.</td>
<td>No</td>
</tr>
<tr>
<td>rid</td>
<td>string</td>
<td>The beneficiary ID or wallet address on the Blockchain.</td>
<td>No</td>
</tr>
<tr>
<td>state</td>
<td>string</td>
<td>The withdrawal state.</td>
<td>No</td>
</tr>
<tr>
<td>confirmations</td>
<td>integer</td>
<td>Number of confirmations.</td>
<td>No</td>
</tr>
<tr>
<td>note</td>
<td>string</td>
<td>Withdraw note.</td>
<td>No</td>
</tr>
<tr>
<td>created_at</td>
<td>string</td>
<td>The datetimes for the withdrawal.</td>
<td>No</td>
</tr>
<tr>
<td>updated_at</td>
<td>string</td>
<td>The datetimes for the withdrawal.</td>
<td>No</td>
</tr>
<tr>
<td>done_at</td>
<td>string</td>
<td>The datetime when withdraw was completed</td>
<td>No</td>
</tr>
</tbody></table>
<h4 id="member"><a class="anchor" name="member" href="#member"><span class="octicon octicon-link"></span></a>Member</h4>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody><tr>
<td>uid</td>
<td>string</td>
<td>Member UID.</td>
<td>No</td>
</tr>
<tr>
<td>email</td>
<td>string</td>
<td>Member email.</td>
<td>No</td>
</tr>
<tr>
<td>accounts</td>
<td>[ <a href="#account">Account</a> ]</td>
<td>Member accounts.</td>
<td>No</td>
</tr>
</tbody></table>
</div></body></html>
