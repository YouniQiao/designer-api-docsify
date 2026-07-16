# ConnectionInfo

Represents the information object of the web native messaging connection.

**Since:** 21

<!--Device-unnamed-export interface ConnectionInfo--><!--Device-unnamed-export interface ConnectionInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { ConnectionInfo } from '@kit.ArkWeb';
```

## bundleName

```TypeScript
bundleName: string
```

Application bundle name of the caller.

**Type:** string

**Since:** 21

<!--Device-ConnectionInfo-bundleName: string--><!--Device-ConnectionInfo-bundleName: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## connectionId

```TypeScript
connectionId: number
```

Connection ID.

**Type:** number

**Since:** 21

<!--Device-ConnectionInfo-connectionId: number--><!--Device-ConnectionInfo-connectionId: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## extensionOrigin

```TypeScript
extensionOrigin: string
```

Original URL of the caller extension.

**Type:** string

**Since:** 21

<!--Device-ConnectionInfo-extensionOrigin: string--><!--Device-ConnectionInfo-extensionOrigin: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## fdRead

```TypeScript
fdRead: number
```

Pipe file descriptor used to read data.

**Type:** number

**Since:** 21

<!--Device-ConnectionInfo-fdRead: number--><!--Device-ConnectionInfo-fdRead: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## fdWrite

```TypeScript
fdWrite: number
```

Pipe file descriptor used to write data.

**Type:** number

**Since:** 21

<!--Device-ConnectionInfo-fdWrite: number--><!--Device-ConnectionInfo-fdWrite: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

