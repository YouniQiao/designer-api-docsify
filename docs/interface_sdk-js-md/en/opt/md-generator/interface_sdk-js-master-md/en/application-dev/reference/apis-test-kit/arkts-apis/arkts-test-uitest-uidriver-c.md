# UiDriver

The **UiDriver** class is the main entry to the UiTest framework. It provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot. All APIs provided by this class, except **UiDriver.create()**, use a promise to return the result and must be invoked using **await**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Driver](arkts-test-uitest-driver-c.md#driver)

<!--Device-unnamed-declare class UiDriver--><!--Device-unnamed-declare class UiDriver-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
```

## assertComponentExist

```TypeScript
assertComponentExist(by: By): Promise<void>
```

Asserts that a component that matches the given attributes exists on the current page. If the component does not exist, the API throws a JS exception, causing the current test case to fail. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [assertComponentExist](arkts-test-uitest-driver-c.md#assertcomponentexist)

<!--Device-UiDriver-assertComponentExist(by: By): Promise<void>--><!--Device-UiDriver-assertComponentExist(by: By): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000003](../errorcode-uitest.md#17000003-assertion-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver, BY } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.assertComponentExist(BY.text('next page'));
}
```

## click

```TypeScript
click(x: number, y: number): Promise<void>
```

Clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [click](arkts-test-uitest-component-c.md#click)

<!--Device-UiDriver-click(x: number, y: number): Promise<void>--><!--Device-UiDriver-click(x: number, y: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.click(100, 100);
}
```

## create

```TypeScript
static create(): UiDriver
```

Creates a **UiDriver** object and returns the object created. This API is a static API. > **NOTE：**> > This method is supported since API version 8 and deprecated since API version 9. You are advised to use > [create&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#create) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [create](arkts-test-uitest-driver-c.md#create)

<!--Device-UiDriver-static create(): UiDriver--><!--Device-UiDriver-static create(): UiDriver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UiDriver](arkts-test-uitest-uidriver-c.md) |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
}
```

## delayMs

```TypeScript
delayMs(duration: number): Promise<void>
```

Delays a duration of time. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [delayMs](arkts-test-uitest-driver-c.md#delayms)

<!--Device-UiDriver-delayMs(duration: number): Promise<void>--><!--Device-UiDriver-delayMs(duration: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.delayMs(1000);
}
```

## doubleClick

```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

Double-clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [doubleClick](arkts-test-uitest-component-c.md#doubleclick)

<!--Device-UiDriver-doubleClick(x: number, y: number): Promise<void>--><!--Device-UiDriver-doubleClick(x: number, y: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.doubleClick(100, 100);
}
```

## findComponent

```TypeScript
findComponent(by: By): Promise<UiComponent>
```

Searches this **UiDriver** object for the target component that matches the given attributes. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [findComponent](arkts-test-uitest-driver-c.md#findcomponent)(on: On)

<!--Device-UiDriver-findComponent(by: By): Promise<UiComponent>--><!--Device-UiDriver-findComponent(by: By): Promise<UiComponent>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.text('next page'));
}
```

## findComponents

```TypeScript
findComponents(by: By): Promise<Array<UiComponent>>
```

Searches this **UiDriver** object for all components that match the given attributes. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [findComponents](arkts-test-uitest-driver-c.md#findcomponents)(on: On)

<!--Device-UiDriver-findComponents(by: By): Promise<Array<UiComponent>>--><!--Device-UiDriver-findComponents(by: By): Promise<Array<UiComponent>>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt;&gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
}
```

## longClick

```TypeScript
longClick(x: number, y: number): Promise<void>
```

Long-clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [longClick](arkts-test-uitest-component-c.md#longclick)

<!--Device-UiDriver-longClick(x: number, y: number): Promise<void>--><!--Device-UiDriver-longClick(x: number, y: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.longClick(100, 100);
}
```

## pressBack

```TypeScript
pressBack(): Promise<void>
```

Presses the Back button on this **UiDriver** object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [pressBack](arkts-test-uitest-driver-c.md#pressback)()

<!--Device-UiDriver-pressBack(): Promise<void>--><!--Device-UiDriver-pressBack(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.pressBack();
}
```

## screenCap

```TypeScript
screenCap(savePath: string): Promise<boolean>
```

Captures the current screen of this **UiDriver** object and saves it as a PNG image to the given save path. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [screenCap](arkts-test-uitest-driver-c.md#screencap)(savePath: string)

<!--Device-UiDriver-screenCap(savePath: string): Promise<boolean>--><!--Device-UiDriver-screenCap(savePath: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| savePath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

## swipe

```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>
```

Swipes on this **UiDriver** object from the start point to the end point based on the given coordinates. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [swipe](arkts-test-uitest-driver-c.md#swipe)

<!--Device-UiDriver-swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>--><!--Device-UiDriver-swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startx | number | Yes |
| starty | number | Yes |
| endx | number | Yes |
| endy | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.swipe(100, 100, 200, 200);
}
```

## triggerKey

```TypeScript
triggerKey(keyCode: number): Promise<void>
```

Triggers a key event by passing the key code value. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [triggerKey](arkts-test-uitest-driver-c.md#triggerkey)(keyCode: int)

<!--Device-UiDriver-triggerKey(keyCode: number): Promise<void>--><!--Device-UiDriver-triggerKey(keyCode: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyCode | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // Back button
}
```
