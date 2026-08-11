# createGZip

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## createGZip

```TypeScript
function createGZip(): Promise<GZip>
```

Creates this **GZip** object. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-zlib-function createGZip(): Promise<GZip>--><!--Device-zlib-function createGZip(): Promise<GZip>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;GZip&gt; | Promise used to return the **GZip** object created. |

## Examples

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

zlib.createGZip().then((data) => {
  console.info('createGZip success');
})
```

