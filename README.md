# streamlit-routing

A sample environment for launching multiple streamlit and proxying from routing to the desired streamlit app.
Streamlit usually accesses `localhost:8901` , `localhost:8902`, etc., but this method is used to access them as `localhost:80/sample1` and `localhost:80/sample2`.

複数のstreamlitを起動し、routingから目的のstreamlit appへプロキシする環境のサンプル。
streamlit は通常 `localhost:8901` , `localhost:8902` などにアクセスするが、これを `localhost:80/sample1` や `localhost:80/sample2` のようにアクセスするための方法。

## Requirements

* [Docker version 17 or later](https://docs.docker.com/install/#support)

## Getting Started
You can check in the following ways.

以下の方法で確認できます。

```terminal
$ make create-image
$ make creatio-container

...open other terminal window

$ open localhost:8888/sample
```


## How to use

### streamlit
First, we create the streamlit app.
We have a separate working directory for each application.

まず、streamlit appを作ります。
各アプリケーションごとに作業ディレクトリを分けるようにしています。

```
src/
├─ sample1/
│  ├─ app.py
├─ sample2/
│  ├─ app.py
├─ <<< add new your working dir >>>
```

The directory name is the name you want to match in the routing.

ディレクトリ名はルーティングでマッチさせたい名前にしています。


### nginx
Add to `nginx.conf` in the same way as `/sample`.

`/sample` と同様に`nginx.conf`に追記していきます。

```docker/nginx/nginx.conf
http {
	server {
		location /sample {
			proxy_pass http://0.0.0.0:8901/sample;
		}

		location /sample/stream {
			proxy_pass http://0.0.0.0:8901/sample/stream;
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
			proxy_http_version 1.1;
			proxy_set_header Upgrade $http_upgrade;
			proxy_set_header Connection "Upgrade";
			proxy_read_timeout 2h;
		}

    <<< add your new routing >>>
	}
}
```


### docker/entrypoint.sh
Finally, add the startup command to `entrypoint.sh`.
Add the path and port number you want to use for startup.
Make sure it doesn't overlap with any other streamlit app.

最後に、`entrypoint.sh`に起動コマンドを追記します。
起動時に使いたいパスとポート番号を書きます。
他のstreamlit app と重複しないようにします。

```entrypoint.sh
#!/bin/bash

nohup streamlit run --server.port=8901 --server.baseUrlPath=sample1 src/sample1/app.py &
nohup streamlit run --server.port=8902 --server.baseUrlPath=sample2 src/sample2/app.py &
<<< add your new streamlit app launching command >>>
service nginx start
```

## How it works
### nginx
単純にnginxのリバースプロキシを使っています。
`docker/nginx/nginx.conf`の`http`ブロックを確認するとわかります。

Simply using nginx's reverse proxy.
It can be seen by checking the `http` block in `docker/nginx/nginx.conf`.

### streamlit
各streamlit appの起動ごとに`basePathConfig` や `port` を指定しています。
ディレクトリに分けているので、重複に気付きやすいです。

For each streamlit app launch, we specify the `basePathConfig` and `port`.
We have separated them into directories, so it's easy to notice the duplication.

# Credits

- This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cookiecutter-docker-science](https://docker-science.github.io/) project template.
- File tree was created with [File tree generator](https://ascii-tree-generator.com)