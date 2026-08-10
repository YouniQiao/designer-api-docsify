# setSync (System API)

## Modules to Import

```TypeScript
import { systemParameterEnhance } from 'kits/@kit.BasicServicesKit';
```

## setSync

```TypeScript
function setSync(key: string, value: string): void
```

设置系统参数key对应的值。

> **说明：**
> 
> setSync和set方法都用于设置系统参数值：
> - setSync：同步方法，直接设置系统参数并立即返回，适用于简单同步场景。
> - set：异步方法，使用callback或Promise异步返回结果，适用于需要异步处理的场景。
> 
> 开发者应根据具体场景选择合适的方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-systemParameterEnhance-function setSync(key: string, value: string): void--><!--Device-systemParameterEnhance-function setSync(key: string, value: string): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待设置的系统参数key。最大长度128字节，只允许字母数字加"."，"-"，"@"，":"或"_"，不允许".."。 |
| value | string | Yes | 待设置的系统参数值。最大长度96字节（包括结束符）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.incorrect parameter types; 3.parameter verification failed. |
| 14700102 | Invalid system parameter value. |
| 14700103 | The operation on the system permission is denied. |
| 14700104 | System internal error such as out memory or deadlock. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    systemParameterEnhance.setSync("test.parameter.key", "default");
} catch(e) {
    console.error("set unexpected error: " + e);
}
```

