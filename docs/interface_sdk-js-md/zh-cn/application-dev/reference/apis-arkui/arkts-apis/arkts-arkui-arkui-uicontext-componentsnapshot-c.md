# ComponentSnapshot

class ComponentSnapshot

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ComponentSnapshot--><!--Device-unnamed-export declare class ComponentSnapshot-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## createFromBuilder

```TypeScript
createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,
    delay?: int, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void
```

Generate a snapshot from a custom component builder.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,    delay?: int, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void--><!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,    delay?: int, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 | Builder function of a custom component. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 | Callback that contains the snapshot in PixelMap format. |
| delay | int | 否 | Defines the delay time to render the snapshot. |
| checkImageStatus | boolean | 否 | Defines if check the image decoding status before taking snapshot. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | The builder is not a valid build function. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |
| 160004 | isAuto(true) is not supported for offscreen node snapshots. |

## createFromBuilder

```TypeScript
createFromBuilder(builder: CustomBuilder, delay?: int,
    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null
```

Generate a snapshot from a custom component builder.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, delay?: int,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null--><!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, delay?: int,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 | Builder function of a custom component. |
| delay | int | 否 | Defines the delay time to render the snapshot. |
| checkImageStatus | boolean | 否 | Defines if check the image decoding status before taking snapshot. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise with the snapshot in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | The builder is not a valid build function. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |
| 160004 | isAuto(true) is not supported for offscreen node snapshots. |

## createFromComponent

```TypeScript
createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: int,
    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null
```

Generate a snapshot from a custom component content.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: int,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null--><!--Device-ComponentSnapshot-createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: int,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | 是 | The content to be taken snapshot. |
| delay | int | 否 | Defines the delay time to render the snapshot. |
| checkImageStatus | boolean | 否 | Defines if check the image decoding status before taking snapshot. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise with the snapshot in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | The builder is not a valid build function. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |
| 160004 | isAuto(true) is not supported for offscreen node snapshots. |

## get

```TypeScript
get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void
```

通过组件id获取组件截图。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void--><!--Device-ComponentSnapshot-get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | Target component ID, set by developer through .id attribute. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 | Callback that contains the snapshot in PixelMap format. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

## get

```TypeScript
get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null
```

通过组件id获取组件截图。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null--><!--Device-ComponentSnapshot-get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | Target component ID, set by developer through .id attribute. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise with the snapshot in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

## getSizeLimitation

```TypeScript
getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation
```

查询组件截图大小限制。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation--><!--Device-ComponentSnapshot-getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| componentSnapshot.SnapshotSizeLimitation | The size limitation for taking a component snapshot. |

## getSync

```TypeScript
getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap | null
```

Take a screenshot of the specified component in synchronous mode,this mode will block the main thread, please use it with caution, the maximum waiting time of the interface is 3s, if it does not return after 3s, an exception will be thrown.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap | null--><!--Device-ComponentSnapshot-getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | Target component ID, set by developer through .id attribute. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | The snapshot result in PixelMap format. Null will be returned if the parameters' checking failed or some internal errors occur, for example: the runtime environment is broken. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID. |
| 160002 | Timeout. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

## getSyncWithUniqueId

```TypeScript
getSyncWithUniqueId(uniqueId: int, options?: componentSnapshot.SnapshotOptions): image.PixelMap
```

Take a screenshot of the specified component in synchronous mode,this mode will block the main thread, please use it with caution, the maximum waiting time of the interface is 3s, if it does not return after 3s, an exception will be thrown.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-getSyncWithUniqueId(uniqueId: int, options?: componentSnapshot.SnapshotOptions): image.PixelMap--><!--Device-ComponentSnapshot-getSyncWithUniqueId(uniqueId: int, options?: componentSnapshot.SnapshotOptions): image.PixelMap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uniqueId | int | 是 | The uniqueId of the node, can get through getUniqueId. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | The snapshot result in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID. |
| 160002 | Timeout. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

## getWithUniqueId

```TypeScript
getWithUniqueId(uniqueId: int, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null
```

通过uniqueId获取组件截图。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-getWithUniqueId(uniqueId: int, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null--><!--Device-ComponentSnapshot-getWithUniqueId(uniqueId: int, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uniqueId | int | 是 | The uniqueId of the node, can get through getUniqueId. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise with the snapshot in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

