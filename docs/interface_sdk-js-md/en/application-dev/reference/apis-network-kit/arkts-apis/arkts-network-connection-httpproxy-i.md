# HttpProxy

Network Global Proxy Configuration Information.

**Since:** 26.0.0

<!--Device-connection-export interface HttpProxy--><!--Device-connection-export interface HttpProxy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## exclusionList

```TypeScript
exclusionList: Array<string>
```

Do not use a blocking list for proxy servers.

**Type:** Array&lt;string&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HttpProxy-exclusionList: Array<string>--><!--Device-HttpProxy-exclusionList: Array<string>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## host

```TypeScript
host: string
```

Proxy server host name.

**Type:** string

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpProxy-host: string--><!--Device-HttpProxy-host: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## password

```TypeScript
password?: string
```

Http proxy password.

**Type:** string

**Since:** 23

<!--Device-HttpProxy-password?: string--><!--Device-HttpProxy-password?: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## port

```TypeScript
port: int
```

Host port.

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpProxy-port: int--><!--Device-HttpProxy-port: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## username

```TypeScript
username?: string
```

Http proxy username.

**Type:** string

**Since:** 23

<!--Device-HttpProxy-username?: string--><!--Device-HttpProxy-username?: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

