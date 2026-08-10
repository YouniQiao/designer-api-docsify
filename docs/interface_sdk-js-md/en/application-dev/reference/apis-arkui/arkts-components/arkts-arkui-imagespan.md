# ImageSpan

ImageSpan是[Text]{@link ./text}、[ContainerSpan]{@link ./container_span}组件的子组件，用于在文本中显示行内图片，支持设置图片对齐方式、缩放类型、加载占位图和颜色滤镜
等，适用于需要在文本段落中嵌入图片实现图文混排的场景。

## 子组件

无

## ImageSpan

```TypeScript
ImageSpan(value: ResourceStr | PixelMap)
```

定义ImageSpan组件构造函数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageSpanInterface-(value: ResourceStr | PixelMap): ImageSpanAttribute--><!--Device-ImageSpanInterface-(value: ResourceStr | PixelMap): ImageSpanAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| PixelMap | Yes | 图片的数据源，支持本地图片和网络图片。 <br>使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考 [声明权限](docroot://security/AccessToken/declare-permissions.md)。 <br>当使用相对路径引用图片资源时，例如`ImageSpan("common/test.jpg")`，不支持跨包/跨模块调用该ImageSpan组件，建议使用`\$r`方式来管理需全局使用的图片资源。 <br>- 支持的图片格式包括png、jpg、bmp、svg、gif、webp和heif。 <br>- 支持`Base64`字符串。格式`data:image/[png\|jpeg\|bmp\|webp\|heif];base64,[base64 data]`，其中`[base64 data]`为`Base64`字符串数 据。 <br>- 支持file://data/storage路径前缀的字符串，用于读取本应用安装目录下file文件夹下的图片资源。需要保证应用安装目录路径下的文件有可读权限。 |

## Summary

- [ImageLoadResult](arkts-arkui-imagespan-imageloadresult-i.md)
- [ImageCompleteCallback](arkts-arkui-imagespan-imagecompletecallback-t.md)
