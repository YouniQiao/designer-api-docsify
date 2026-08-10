# DepthMapCallback (System API)

```TypeScript
export declare type DepthMapCallback = (error: BusinessError<void>) => void
```

深度图资源加载完成时的回调函数。使用callback异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type DepthMapCallback = (error: BusinessError<void>) => void--><!--Device-unnamed-export declare type DepthMapCallback = (error: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | Yes | 深度图资源加载完成时返回的错误信息。加载成功时error.code为0，加载失败时error中包含错误码和错误信息。 |

