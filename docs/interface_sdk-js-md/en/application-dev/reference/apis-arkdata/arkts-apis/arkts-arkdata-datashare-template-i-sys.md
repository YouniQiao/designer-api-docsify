# Template (System API)

Defines the struct of the template used in a subscription.

**Since:** 10

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dataShare } from '@kit.ArkData';
```

## predicates

```TypeScript
predicates: Record<string, string>
```

Predicates to use. When **on** is called, the predicates are used to generate data. This parameter applies only to RDB data storage.

**Type:** Record&lt;string, string&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## scheduler

```TypeScript
scheduler: string
```

Template scheduler SQL, which is embedded with a custom function. Currently, the **remindTimer** function is embedded. The **remindTimer** triggers a subscription-based update in specified scenarios.

The scheduler SQL statement is triggered when:

1. The subscribed data is modified.
2. The first subscription is added to the corresponding database.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## update

```TypeScript
update?: string
```

Update SQL statement of a specified template. The default value is an empty string. When on is called, the **update** parameter is used to update data. This parameter applies only to RDB data storage.

**Type:** string

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Examples**

```TypeScript
import { dataSharePredicates, ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
let key1: string = "name";
let value1: string = "roe1";
let key2: string = "age";
let value2: number = 21;
let key3: string = "salary";
let value3: number = 20.5;
const va: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
};
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).update(uri, da, va, (err: BusinessError, data: number) => {
      if (err !== undefined) {
        console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info("update succeed, data : " + data);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to update. Code: ${code}, message: ${message}`);
}
```

```TypeScript
import { dataSharePredicates, ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
let key1: string = "name";
let value1: string = "roe1";
let key2: string = "age";
let value2: number = 21;
let key3: string = "salary";
let value3: number = 20.5;
const va: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
};
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).update(uri, da, va).then((data: number) => {
      console.info("update succeed, data : " + data);
    }).catch((err: BusinessError) => {
      console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to update. Code: ${code}, message: ${message}`);
}
```
