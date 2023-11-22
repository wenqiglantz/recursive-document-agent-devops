# Guide / API Keys

API keys allow you to access a specific repository via the API without having 
to follow a login process.

You may create API keys via the CLI, the Web UI, or, once you have an API Key, via the API.
All API keys expire, and the maximum duration of a key is 90 days.

## Creating an API Key

From the command line, once you have logged in, you can request a token:

```shell
$ pd apikey create --expire 30 --description "this is my new key"
KeyID: 01H1QFS29DR9G2CY9KM8VW1E8X
Token: v2.public.eyJleHAiOiIyMDIzLTA2LTI5VDE2OjI3OjAzLTA3OjBwIiwiaHViaWQiOiIwMUgxTVBQQ...
```

If you don't specify an expiration the default value of 30 days is used. Expired keys cannot be used.

The Token value will only be displayed a single time. The key is not persisted within the 
Provenant Data platform, and cannot be retrieved at a later time. Make sure you record
the token when it is issued.

## Viewing Existing Keys

You can see all keys issued to the current user:

```shell
 $ pd apikey list
 ID                         Description          Enabled Revoked LastUsed   Expires
 01H1MXM93PRVZNMNN70RAHCPVT no description       true    true    never used 2023-06-28 23:31:23.895445 +0000 UTC
 01H1N18NFW7F85848P15DD8ZRZ no description       true    true    never used 2023-06-29 00:34:57.661359 +0000 UTC
 01H1QE546GD2S68376T67M3Y9P this is a descrip... true    false   never used 2023-06-29 22:58:42.000543 +0000 UTC
 01H1MXB5TRQR828F22JMSQJP43 no description       true    true    never used 2023-06-28 23:26:25.624826 +0000 UTC
 01H1N1CDRDQ75C8W40P40RK8FM no description       true    false   never used 2023-06-29 00:37:00.814444 +0000 UTC
```

To see more detail on a specific key, reference it by its ID:

```shell
$ pd apikey show 01H1MXM93PRVZNMNN70RAHCPVT
Key ID:      01H1MXM93PRVZNMNN70RAHCPVT
Description: no description
Last Used:   never used
Expires:     2023-06-28 23:31:23.895445 +0000 UTC
```

## Revoking an API Key

To permanently revoke a key, use the `pd apikey revoke` command:

```shell
i pd apikey revoke 01H1MXB5TRQR828F22JMSQJP43 --comment 'revoking key'
KeyID: 01H1MXB5TRQR828F22JMSQJP43 revoked
```

The key will now show as revoked:

```shell
$ pd apikey show 01H1MXB5TRQR828F22JMSQJP43
Key ID:      01H1MXB5TRQR828F22JMSQJP43 (revoked)
Description: no description
Last Used:   never used
Expires:     2023-06-28 23:26:25.624826 +0000 UTC
```

Once a key is revoked, it may never be used again. 


## Using an API Key

In order to use the API key, pass the token into the GRPC call as credential metadata. 

See for example, see this Python fragment below:

```Python
with grpc.secure_channel(
    "localhost:8000",
    # And here, we pass the token which will authenticate this
    # api call
    grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(cert),
        grpc.metadata_call_credentials(GrpcAuth(token)),
    ),
) as channel:
    stub = metadata_pb2_grpc.MetadataServiceStub(channel)
    list_branches(stub)

# etc.
```

The same basic process is followed in this Go fragment:

```Go
// Token-based authentication sends sends the token in an authorization header.
// We need to implement the grpc/credentials.PerRPCCredentials
// (https://pkg.go.dev/google.golang.org/grpc/credentials?utm_source=godoc#PerRPCCredentials)
// in order to transmit the token.
type tokenAuth struct {
	token string
}

func (t tokenAuth) GetRequestMetadata(ctx context.Context, in ...string) (map[string]string, error) {
	return map[string]string{
		"Authorization": "Bearer " + t.token,
	}, nil
}

func (t tokenAuth) RequireTransportSecurity() bool {
	return true
}

func setupConn(token string) *grpc.ClientConn {  // <--- pass token into setup function
	const maxSize = 1024 * 1024 * 100 // 100MB. Arbitrary value for the purpose of demonstration
	dialOpts := []grpc.DialOption{
		grpc.WithDefaultCallOptions(
			grpc.MaxCallRecvMsgSize(maxSize),
			grpc.UseCompressor(gzip.Name),
		),
	}

  // supply token to GRPC Credential
	dialOpts = append(dialOpts, grpc.WithPerRPCCredentials(tokenAuth{token: token})) 
	tlsCreds := &tls.Config{
		// Do not verify the self-signed certificates used in the PD docker demo
		// environment. In deployed environments valid certs are used, and we do
		// not need to skip verification.
		InsecureSkipVerify: true,
	}
	dialOpts = append(dialOpts, grpc.WithTransportCredentials(credentials.NewTLS(tlsCreds)))

	conn, err := grpc.DialContext(
		context.Background(),
		"localhost:8000", // By default, the gRPC interface listens on 8000
		dialOpts...,
	)
	if err != nil {
		log.Fatal(err)
	}

	return conn
}
```

See the [API documentation](/docs/api) for more guidance on using the Provenant
Data API. And see the [CLI Reference](/docs/commands/pd_apikey.html) for more info on
the `pd apikeys` command.
