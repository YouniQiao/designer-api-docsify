# App

定义App类的静态函数

**起始版本：** 3

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## 导入模块

```TypeScript
import { App, AppResponse, RequestFullWindowOptions, ScreenOnVisibleOptions } from 'kits/@kit.ArkUI';
```

## getInfo

```TypeScript
static getInfo(): AppResponse
```

获取当前应用配置文件中声明的信息。在Stage模型下接口返回值为null。从API version9开始，推荐使用 [bundleManager.getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md) 。

**起始版本：** 3

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

| 类型 |
| --- |
| [AppResponse](arkts-arkui-system-app-appresponse-i.md) |

## requestFullWindow

```TypeScript
static requestFullWindow(options?: RequestFullWindowOptions): void
```

Requests the application to run in full window. In some scenarios, such as semi-modal FA, the FA runs in non-full window. In this case, you can call this API. This API is invalid for an application already in full-window mode.

**起始版本：** 3

**废弃版本：** 8

**替代接口：** startAbility

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RequestFullWindowOptions](arkts-arkui-system-app-requestfullwindowoptions-i.md) | 否 |

## screenOnVisible

```TypeScript
static screenOnVisible(options?: ScreenOnVisibleOptions): void
```

定义屏幕唤醒时是否保持应用可见。该接口从API version 8 开始废弃。

**起始版本：** 3

**废弃版本：** 8

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ScreenOnVisibleOptions](arkts-arkui-system-app-screenonvisibleoptions-i.md) | 否 |

## setImageCacheCount

```TypeScript
static setImageCacheCount(value: number): void
```

Set image cache capacity of decoded image count. if not set, the application will not cache any decoded image.

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setImageFileCacheSize

```TypeScript
static setImageFileCacheSize(value: number): void
```

设置图像文件在解码前在磁盘上的缓存大小（字节）。如果未设置，应用程序将在磁盘上缓存 100MB 的图像文件。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setImageRawDataCacheSize

```TypeScript
static setImageRawDataCacheSize(value: number): void
```

Set image cache capacity of raw image data size in bytes before decode. if not set, the application will not cache any raw image data.

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## terminate

```TypeScript
static terminate(): void
```

退出当前Ability。在Stage模型下接口功能不生效。从API version 7开始，推荐使用[`@ohos.ability.featureAbility`](../../apis-ability-kit/arkts-apis/arkts-ability-featureability.md)。

**起始版本：** 3

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite
