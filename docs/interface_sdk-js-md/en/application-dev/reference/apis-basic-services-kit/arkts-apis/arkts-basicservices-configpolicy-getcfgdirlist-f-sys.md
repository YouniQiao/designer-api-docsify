# getCfgDirList (System API)

## Modules to Import

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgDirList

```TypeScript
function getCfgDirList(callback: AsyncCallback<Array<string>>): void
```

Obtains a list of configuration level directories, in ascending order of priority. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

configPolicy.getCfgDirList((err: BusinessError, data: Array<string>) => {
  if (err == null) {
    console.info('data is ' + data);
  } else {
    console.error('err: ' + err.code + ', ' + err.message);
  }
});
```

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

async function fetchCfgDirList() {
  try {
    let value: Array<string> = await configPolicy.getCfgDirList();
    console.info('value is ' + value);
  } catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error('error:' + code + ', ' + message);
  }
}

fetchCfgDirList();
```


## getCfgDirList

```TypeScript
function getCfgDirList(): Promise<Array<string>>
```

Obtains a list of configuration level directories, in ascending order of priority. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Examples**

See [getCfgDirList](#getcfgdirlist)
