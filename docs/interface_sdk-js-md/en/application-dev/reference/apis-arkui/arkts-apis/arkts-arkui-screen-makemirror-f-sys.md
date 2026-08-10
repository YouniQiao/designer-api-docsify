# makeMirror (System API)

## makeMirror

```TypeScript
function makeMirror(mainScreen:long, mirrorScreen:Array<long>, callback: AsyncCallback<long>): void
```

Sets the screen to mirror mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>, callback: AsyncCallback<long>): void--><!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mainScreen | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | ID of the primary screen. The ID must be a non-negative integer. |
| mirrorScreen | ArkTS-Dyn: Array&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Array&lt;long&gt; | Yes | Array of IDs of secondary screens. Each ID must be a positive integer. |
| callback | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;long&gt; | Yes | Callback used to return the group ID of the secondary screens, where the ID is a positive integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let mainScreenId: number = 0;
let mirrorScreenIds: Array<number> = [1, 2, 3];
screen.makeMirror(mainScreenId, mirrorScreenIds, (err: BusinessError, data: number) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set screen mirroring. Code:${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting screen mirroring. Data: ${data}`);
});
```


## makeMirror

```TypeScript
function makeMirror(mainScreen:long, mirrorScreen:Array<long>): Promise<long>
```

Sets the screen to mirror mode. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>): Promise<long>--><!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>): Promise<long>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mainScreen | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | ID of the primary screen. The ID must be a non-negative integer. |
| mirrorScreen | ArkTS-Dyn: Array&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Array&lt;long&gt; | Yes | Array of IDs of secondary screens. Each ID must be a positive integer. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;long&gt; | Promise used to return the group ID of the secondary screens, where the ID is a positive integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let mainScreenId: number = 0;
let mirrorScreenIds: Array<number> = [1, 2, 3];
screen.makeMirror(mainScreenId, mirrorScreenIds).then((data: number) => {
  console.info(`Succeeded in setting screen mirroring. Data: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set screen mirroring. Code:${err.code}, message is ${err.message}`);
});
```

