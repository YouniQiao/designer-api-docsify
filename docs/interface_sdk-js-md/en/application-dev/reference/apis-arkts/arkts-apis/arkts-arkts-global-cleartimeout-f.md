# clearTimeout

## clearTimeout

```TypeScript
function clearTimeout(timerId?: int | null): void
```

取消指定的定时器。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function clearTimeout(timerId?: int | null): void--><!--Device-unnamed-function clearTimeout(timerId?: int | null): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timerId | int \| null | No | 由setTimeout返回的定时器ID， 如果不传、传入null或undefined，则不执行任何操作。 |

