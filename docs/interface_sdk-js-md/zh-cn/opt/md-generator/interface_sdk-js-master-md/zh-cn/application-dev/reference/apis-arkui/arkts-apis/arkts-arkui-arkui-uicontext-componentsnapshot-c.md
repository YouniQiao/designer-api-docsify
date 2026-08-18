# ComponentSnapshot

提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。 > **说明：** > > - 本Class首批接口从API version 12开始支持。 > > - 以下API需先使用UIContext中的[getComponentSnapshot()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)方法获取ComponentSnapshot对象，再通过此实例调用对应方法。 > > - 缩放、平移、旋转等图形变换属性只对被截图组件的子组件生效；对目标组件本身应用图形变换属性不生效，显示的还是图形变换前的效果。

**起始版本：** 12

<!--Device-unnamed-export class ComponentSnapshot--><!--Device-unnamed-export class ComponentSnapshot-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## createFromBuilder

```TypeScript
createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,
    delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void
```

传入[CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md#custombuilder)自定义组件，系统对其进行离屏构建后进行截图。使用callback异步回调。 > **说明：** > > - 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟，不适宜使用在对性能敏感的场景。 > > - 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的Image组件、Web组件。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,    delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void--><!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,    delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |
| delay | number | 否 |
| checkImageStatus | boolean | 否 |
| options | componentSnapshot.SnapshotOptions | 否 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |
| [160001](../errorcode-snapshot.md#160001-图像加载错误) |
| [160004](../errorcode-snapshot.md#160004-离屏节点截图不支持将色彩空间或动态范围模式对应的isauto参数设置为true) |

## createFromBuilder

```TypeScript
createFromBuilder(builder: CustomBuilder, delay?: number,
    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

传入[CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md#custombuilder)自定义组件，系统对其进行离屏构建后进行截图。使用Promise异步回调。 > **说明：** > > - 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟，不适宜使用在对性能敏感的场景。 > > - 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的Image组件、Web组件。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, delay?: number,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>--><!--Device-ComponentSnapshot-createFromBuilder(builder: CustomBuilder, delay?: number,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 |
| delay | number | 否 |
| checkImageStatus | boolean | 否 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |
| [160001](../errorcode-snapshot.md#160001-图像加载错误) |
| [160004](../errorcode-snapshot.md#160004-离屏节点截图不支持将色彩空间或动态范围模式对应的isauto参数设置为true) |

## createFromComponent

```TypeScript
createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: number,
    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

将传入的content对象进行截图。使用Promise异步回调。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: number,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>--><!--Device-ComponentSnapshot-createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: number,    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | ComponentContent & lt;T & gt; | 是 |
| delay | number | 否 |
| checkImageStatus | boolean | 否 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |
| [160001](../errorcode-snapshot.md#160001-图像加载错误) |
| [160004](../errorcode-snapshot.md#160004-离屏节点截图不支持将色彩空间或动态范围模式对应的isauto参数设置为true) |

## get

```TypeScript
get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void
```

获取已加载的组件的截图，传入组件的组件标识，找到对应组件进行截图。使用callback异步回调。 > **说明：** > > 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void--><!--Device-ComponentSnapshot-get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |
| options | componentSnapshot.SnapshotOptions | 否 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |

## get

```TypeScript
get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

获取已加载的组件的截图，传入组件的组件标识，找到对应组件进行截图。使用Promise异步回调。 > **说明：** > > 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>--><!--Device-ComponentSnapshot-get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |

## getSizeLimitation

```TypeScript
getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation
```

查询组件截图的最大尺寸限制。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation--><!--Device-ComponentSnapshot-getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| componentSnapshot.SnapshotSizeLimitation |

## getSync

```TypeScript
getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap
```

获取已加载的组件的截图。传入组件的组件标识，找到对应组件进行截图，同步等待截图完成返回[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md#pixelmap)。 本方法会阻塞主线程，请谨慎使用。接口的最大等待时间为3s，如果3s后未返回将会抛出异常。 > **说明：** > > 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap--><!--Device-ComponentSnapshot-getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [160002](../errorcode-snapshot.md#160002-截图超时) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |

## getSyncWithUniqueId

```TypeScript
getSyncWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): image.PixelMap
```

获取已加载的组件的截图，传入组件的uniqueId，找到对应组件进行截图。同步等待截图完成返回[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md#pixelmap)。 > **说明：** > > 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-getSyncWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): image.PixelMap--><!--Device-ComponentSnapshot-getSyncWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): image.PixelMap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uniqueId | number | 是 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [160002](../errorcode-snapshot.md#160002-截图超时) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |

## getWithUniqueId

```TypeScript
getWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

获取已加载的组件的截图，传入组件的uniqueId，找到对应组件进行截图。使用Promise异步回调。 > **说明：** > > 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-ComponentSnapshot-getWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>--><!--Device-ComponentSnapshot-getWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uniqueId | number | 是 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |
