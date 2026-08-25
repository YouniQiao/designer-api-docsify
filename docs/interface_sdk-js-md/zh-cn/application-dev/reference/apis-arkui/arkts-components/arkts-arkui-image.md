# Image

Image为图片组件，常用于在应用中显示图片。Image支持加载[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)、 ResourceStr和[DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md)类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif 、heif和tiff类型的图片格式，不支持apng和svga格式。
> **说明：**>> - 从API version 23开始，图片类型新增支持tiff格式。>> - 该组件从API版本26.0.0开始支持WithTheme。>> - 使用快捷组合键对Image组件复制时，Image组件必须处于获焦状态，如何获焦请参考[设置组件是否可获焦](../../../ui/arkts-common-events-focus-event.md#设置组件是否可获焦)。> Image组件默认不获焦，需将focusable属性设置为true，即可使用Tab键将焦点切换到组件上，再将> focusOnTouch属性设置为true，即可实现点击获焦。>> - 图片格式支持SVG图源，SVG标签文档请参考SVG标签说明。>> - 动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，通过回调启动动画，当节点不可见时，停止动画。可见性状态的判断是通过> onVisibleAreaChange> 事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。>> - Image组件播放GIF动图时，帧时长取自GIF文件中各帧的delay time字段。当某帧的时长值小于等于0时，系统会将其修正为100ms；当某帧的时长值大于0时，系统直接使用该原始值，不做最小帧时长限制。
需要权限
使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../../../security/AccessToken/declare-permissions.md)。
子组件
无

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor)
```

通过图片数据源获取图片，用于后续渲染展示。Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。Image加载成功且组件不设置宽高时，其显示大小自适应父组件。

> **说明：**&gt;
> - Image直接传入URL可能会带来的潜在性能问题，例如：(1) 大图加载时无法提前下载，白块显示的时间较长；(2) 小图设置同步加载，在弱网环境下，可能会阻塞UI线程造成冻屏问题；(3) 在快速滑动的瀑布流中，无法提前对即
> 将要显示的图片进行下载，导致滑动白块较多。不同场景下，性能问题会有不同的表现，建议将网络下载部分与Image的显示剥离，可提前下载或者异步下载。&gt;
> - src由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。&gt;
> - 当Image组件入参为[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)类型时，只有当PixelMap对象发生变化（即指向一个新的PixelMap实例），
> Image组件才能感知到数据的变化。仅修改PixelMap对象的内容（如像素值）而不更换对象引用，无法触发数据变化的感知。&gt;
> - Image组件入参为Base64字符串时，Base64字符串通用格式为`data:image/subtype;base64,Base64EncodedData`，其中subtype为类型声明，Base64
> EncodedData为数据对应的base64编码，其他为固定字符串。例如：png图像对应的入参为`data:image/png;base64,iVBORw0KGgo...`。&gt;
> 1. image/subType用于声明数据内容的类型。从API版本26.0.0开始，Image组件接受任意`data:image/xxx;base64,Base64EncodedData`格式的Base64字符串，具体图片类
> 型由系统多媒体能力根据实际数据内容识别，无需枚举所有支持的MIME类型。对于API版本26.0.0之前版本，Image组件不会强制校验声明的类型与Base64解码后的实际图片格式是否完全一致。在部分场景下，即使声明的类型与真实
> 格式不一致，图片仍可能正常显示。为避免未来行为变化或未知问题，建议始终保持类型与实际图片格式一致。&gt;
> 2. Image组件从API版本26.0.0开始支持通过`data:image/*;base64,Base64EncodedData`的通配写法，对于API版本26.0.0之前版本，Image组件不支持
> `data:image/*;base64,Base64EncodedData`的通配写法，subType必须显式声明具体的图片类型。&gt;
> 3. Image组件从API版本26.0.0开始支持通过Base64加载SVG图片，对于API版本26.0.0之前版本，Image组件不支持通过Base64字符串形式加载SVG图片。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| src | PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | 是 |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)
```

src新增[ImageContent](arkts-arkui-imagecontent-e.md)类型，可指定对应的图形内容。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| src | PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) \| [ImageContent](arkts-arkui-imagecontent-e.md) | 是 |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string)
```

获取图片，支持通过reloadKey参数触发图片重新加载。当reloadKey的值发生变化时，将不使用缓存重新加载图片。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| src | PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) \| [ImageContent](arkts-arkui-imagecontent-e.md) | 是 |
| reloadKey | string | 否 |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)
```

Image新增ImageAIOptions参数，为组件设置AI分析选项。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| src | PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | 是 |
| imageAIOptions | [ImageAIOptions](../arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | 是 |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor,
      imageAIOptions?: ImageAIOptions, reloadKey?: string)
```

获取图片，支持通过ImageAIOptions参数设置AI分析选项。当reloadKey的值发生变化时，将不使用缓存重新加载图片。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| src | PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | 是 |
| imageAIOptions | [ImageAIOptions](../arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |
| reloadKey | string | 否 |

## 汇总

### 接口

| 名称 |
| --- |

### 类型

| 名称 |
| --- |
| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) |
| [DrawingLattice](arkts-arkui-drawinglattice-t.md) |
| [ImageErrorCallback](arkts-arkui-imageerrorcallback-t.md) |
| [ImageMatrix](arkts-arkui-imagematrix-t.md) |
| [RequestDownloadInfo](arkts-arkui-requestdownloadinfo-t.md) |
| [ResolutionQuality](arkts-arkui-resolutionquality-t-sys.md) |

### 枚举

| 名称 |
| --- |
