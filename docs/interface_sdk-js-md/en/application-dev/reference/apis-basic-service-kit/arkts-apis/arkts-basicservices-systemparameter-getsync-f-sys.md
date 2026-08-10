# getSync (System API)

## Modules to Import

```TypeScript
import { systemParameter } from 'kits/@kit.BasicServicesKit';
```

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

获取系统参数key对应的值。

> **说明：**
> 
> getSync和get方法都用于获取系统参数值：
> - getSync：同步方法，直接返回系统参数值，适用于简单同步场景。
> - get：异步方法，使用callback或Promise异步返回结果，适用于需要异步处理的场景。
> 
> 开发者应根据具体场景选择合适的方法。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.systemParameterEnhance.getSync

<!--Device-systemParameter-function getSync(key: string, def?: string): string--><!--Device-systemParameter-function getSync(key: string, def?: string): string-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待查询的系统参数key。 |
| def | string | No | def为所要获取的系统参数的默认值。 &lt;br&gt; def为可选参数，仅当系统参数不存在时生效。 &lt;br&gt;def可以传undefined或自定义的任意值。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 系统参数值。 &lt;br&gt; 若key存在,返回设定的值。 &lt;br&gt; 若key不存在且def有效，返回def；若未指定def或def无效(如undefined)，返回空字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.incorrect parameter types; 3.parameter verification failed. |
| 14700102 | Invalid system parameter value. |
| 14700103 | The operation on the system permission is denied. |
| 14700104 | System internal error such as out memory or deadlock. |

## Examples

```TypeScript
try {
    let info: string = systemParameter.getSync("const.ohos.apiversion");
    console.info(JSON.stringify(info));
} catch(e) {
    console.error("getSync unexpected error: " + e);
}
```

