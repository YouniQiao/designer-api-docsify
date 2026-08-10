# OnCompletedFn

```TypeScript
type OnCompletedFn = (error: BusinessError<void>) => void
```

所有启动任务完成时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnCompletedFn = (error: BusinessError<void>) => void--><!--Device-unnamed-type OnCompletedFn = (error: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | Yes | 错误信息。 |

