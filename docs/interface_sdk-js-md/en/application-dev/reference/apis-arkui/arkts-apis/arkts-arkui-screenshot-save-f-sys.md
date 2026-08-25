# save (System API)

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## save

```TypeScript
function save(options: ScreenshotOptions, callback: AsyncCallback<image.PixelMap>): void
```

Obtains a screenshot. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** 
- API version 26.0.0+: ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 22 - 24: ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 7 - 21: ohos.permission.CAPTURE_SCREEN

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ScreenshotOptions](arkts-arkui-screenshot-screenshotoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |


## save

```TypeScript
function save(callback: AsyncCallback<image.PixelMap>): void
```

Obtains a screenshot. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** 
- API version 26.0.0+: ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 22 - 24: ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 7 - 21: ohos.permission.CAPTURE_SCREEN

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## save

```TypeScript
function save(options?: ScreenshotOptions): Promise<image.PixelMap>
```

Obtains a screenshot. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** 
- API version 26.0.0+: ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 22 - 24: ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 7 - 21: ohos.permission.CAPTURE_SCREEN

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ScreenshotOptions](arkts-arkui-screenshot-screenshotoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
