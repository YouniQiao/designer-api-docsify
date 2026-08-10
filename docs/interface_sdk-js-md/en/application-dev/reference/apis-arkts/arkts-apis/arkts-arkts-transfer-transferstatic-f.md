# transferStatic

## Modules to Import

```TypeScript
import { transfer } from 'kits/@kit.ArkTS';
```

## transferStatic

```TypeScript
function transferStatic(input: Any, inputName: string): Object
```

将1.0对象转换为1.2对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-transfer-function transferStatic(input: Any, inputName: string): Object--><!--Device-transfer-function transferStatic(input: Any, inputName: string): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Any | Yes | 需要转换的1.0对象。 |
| inputName | string | Yes | 子系统注册的名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 转换后的对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200067 | 转换错误，不支持的输入名称！ |

