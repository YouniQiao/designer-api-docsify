# Screen (System API)

Defines the [physical screen](../../../displaymanager/display-terminology.md#physical-screen) instance.Before calling any API in Screen, you must use [getAllScreens()](arkts-arkui-screen-getallscreens-f-sys.md) or [createVirtualScreen()](arkts-arkui-screen-createvirtualscreen-f-sys.md) to obtain a Screen instance.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## setDensityDpi

```TypeScript
setDensityDpi(densityDpi: number, callback: AsyncCallback<void>): void
```

Sets the pixel density of the screen. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [densityDpi](arkts-arkui-screen-screen-i-sys.md) | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## setDensityDpi

```TypeScript
setDensityDpi(densityDpi: number): Promise<void>
```

Sets the pixel density of the screen. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [densityDpi](arkts-arkui-screen-screen-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## setOrientation

```TypeScript
setOrientation(orientation: Orientation, callback: AsyncCallback<void>): void
```

Sets the screen orientation. This API uses an asynchronous callback to return the result. The screen orientation changes only when the specified orientation complies with the [application rotation policy](../../../quick-start/module-configuration-file.md#abilities) (you can configure the application rotation policy by setting the **orientation** field in the **abilities** tag in the **module.json5** file). If the specified orientation does not comply with the application rotation policy, the screen orientation does not change and no exception is thrown.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [orientation](#orientation) | [Orientation](#orientation) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## setOrientation

```TypeScript
setOrientation(orientation: Orientation): Promise<void>
```

Sets the screen orientation. This API uses a promise to return the result. The screen orientation changes only when the specified orientation complies with the [application rotation policy](../../../quick-start/module-configuration-file.md#abilities) (you can configure the application rotation policy by setting the **orientation** field in the **abilities** tag in the **module.json5** file). If the specified orientation does not comply with the application rotation policy, the screen orientation does not change and no exception is thrown.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [orientation](#orientation) | [Orientation](#orientation) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## setOrientation

```TypeScript
setOrientation(orientation: Orientation, orientationOptions?: OrientationOptions): Promise<void>
```

Set the orientation of the screen

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [orientation](#orientation) | [Orientation](#orientation) | Yes |
| orientationOptions | [OrientationOptions](arkts-arkui-screen-orientationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## setScreenActiveMode

```TypeScript
setScreenActiveMode(modeIndex: number, callback: AsyncCallback<void>): void
```

Sets the active mode of the screen. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modeIndex | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## setScreenActiveMode

```TypeScript
setScreenActiveMode(modeIndex: number): Promise<void>
```

Sets the active mode of the screen. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modeIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## activeModeIndex

```TypeScript
readonly activeModeIndex: number
```

Index of the active screen mode. The current value and value range of this parameter vary according to the screen resolution, refresh rate, and device hardware. The value is an integer.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## densityDpi

```TypeScript
readonly densityDpi?: number
```

Physical pixel density of the screen, that is, the number of pixels per inch.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## id

```TypeScript
readonly id: number
```

Screen ID, which is an integer.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## isInUse

```TypeScript
readonly isInUse?: boolean
```

The screen is in use

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## orientation

```TypeScript
readonly orientation: Orientation
```

Screen orientation.

**Type:** Orientation

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## parent

```TypeScript
readonly parent: number
```

ID of the group to which a screen belongs, where the ID is an integer.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## rsId

```TypeScript
readonly rsId: number
```

Screen port ID, which is an integer.

**Type:** number

**Since:** 21

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## screenType

```TypeScript
readonly screenType?: ScreenType
```

Screen type.

**Type:** [ScreenType](arkts-arkui-screen-screentype-e-sys.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## serialNumber

```TypeScript
readonly serialNumber?: string
```

Serial number of the extended screen. By default, the value is an empty string.

**Type:** string

**Since:** 15

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## sourceMode

```TypeScript
readonly sourceMode: ScreenSourceMode
```

Source mode of the screen

**Type:** [ScreenSourceMode](arkts-arkui-screen-screensourcemode-e-sys.md)

**Since:** 10

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## supportedModeInfo

```TypeScript
readonly supportedModeInfo: Array<ScreenModeInfo>
```

Mode set supported by the screen.

**Type:** Array&lt;[ScreenModeInfo](arkts-arkui-screen-screenmodeinfo-i-sys.md)&gt;

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.
