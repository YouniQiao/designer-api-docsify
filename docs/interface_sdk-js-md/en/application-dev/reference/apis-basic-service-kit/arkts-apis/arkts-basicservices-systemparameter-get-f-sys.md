# get (System API)

## Modules to Import

```TypeScript
import { systemParameter } from 'kits/@kit.BasicServicesKit';
```

## get

```TypeScript
function get(key: string, callback: AsyncCallback<string>): void
```

获取系统参数key对应的值，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.systemParameterEnhance.get

<!--Device-systemParameter-function get(key: string, callback: AsyncCallback<string>): void--><!--Device-systemParameter-function get(key: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待查询的系统参数Key。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，用于异步返回系统参数值。当获取成功时，err为undefined，data为系统参数值；当获取失败时，err为错误对象，data为undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.incorrect parameter types; 3.parameter verification failed. |
| 14700102 | Invalid system parameter value. |
| 14700103 | The operation on the system permission is denied. |
| 14700104 | System internal error such as out memory or deadlock. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';

try {
    systemParameter.get("const.ohos.apiversion", (err: BusinessError, data: string) => {
    if (err == undefined) {
        console.info("get test.parameter.key value success:" + data)
    } else {
        console.error(" get test.parameter.key value err:" + err.code)
    }});
} catch(e) {
    console.error("get unexpected error: " + e);
}
```


## get

```TypeScript
function get(key: string, def: string, callback: AsyncCallback<string>): void
```

获取系统参数key对应的值，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.systemParameterEnhance.get

<!--Device-systemParameter-function get(key: string, def: string, callback: AsyncCallback<string>): void--><!--Device-systemParameter-function get(key: string, def: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待查询的系统参数key。 |
| def | string | Yes | def为所要获取的系统参数的默认值。调用时必须传入此参数，但参数值可以传任意字符串类型的值。仅当系统参数不存在时，def参数值生效。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，用于异步返回系统参数值。当获取成功时，err为undefined，data为系统参数值；当获取失败时，err为错误对象，data为undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.incorrect parameter types; 3.parameter verification failed. |
| 14700102 | Invalid system parameter value. |
| 14700103 | The operation on the system permission is denied. |
| 14700104 | System internal error such as out memory or deadlock. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';

try {
    systemParameter.get("const.ohos.apiversion", "default", (err: BusinessError, data: string) => {
        if (err == undefined) {
            console.info("get test.parameter.key value success:" + data)
        } else {
            console.error(" get test.parameter.key value err:" + err.code)
        }
    });
} catch(e) {
    console.error("get unexpected error:" + e)
}
```


## get

```TypeScript
function get(key: string, def?: string): Promise<string>
```

获取系统参数key对应的值，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.systemParameterEnhance.get

<!--Device-systemParameter-function get(key: string, def?: string): Promise<string>--><!--Device-systemParameter-function get(key: string, def?: string): Promise<string>-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待查询的系统参数key。 |
| def | string | No | def为所要获取的系统参数的默认值。 &lt;br&gt; def为可选参数，仅当系统参数不存在时生效。 &lt;br&gt; def可以传undefined或任意字符串类型的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise示例，用于异步获取结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.incorrect parameter types; 3.parameter verification failed. |
| 14700102 | Invalid system parameter value. |
| 14700103 | The operation on the system permission is denied. |
| 14700104 | System internal error such as out memory or deadlock. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';

try {
    let p: Promise<string> = systemParameter.get("const.ohos.apiversion");
    p.then((value: string) => {
        console.info("get test.parameter.key success: " + value);
    }).catch((err: BusinessError) => {
        console.error("get test.parameter.key error: " + err.code);
    });
} catch(e) {
    console.error("get unexpected error: " + e);
}
```

