# InputType

Declare the type of input box

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum InputType--><!--Device-unnamed-export declare enum InputType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Normal

```TypeScript
Normal = 0
```

Basic input mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-Normal = 0--><!--Device-InputType-Normal = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NUMBER

```TypeScript
NUMBER = 2
```

Pure digital input mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-NUMBER = 2--><!--Device-InputType-NUMBER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PhoneNumber

```TypeScript
PhoneNumber = 3
```

Phone number entry mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-PhoneNumber = 3--><!--Device-InputType-PhoneNumber = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Email

```TypeScript
Email = 5
```

E-mail address input mode.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This mode accepts only digits, letters, underscores (_), dots (.), and the following special characters: ! # \$ % & ' " + - / = ? ^ ` { | } ~ @ (which can only appear once) </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-Email = 5--><!--Device-InputType-Email = 5-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Password

```TypeScript
Password = 7
```

Password entry mode.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>An eye icon is used to show or hide the password. <br>By default, the entered characters are temporarily shown before being obscured by dots; they are directly obscured by dots since API version 12 on certain devices. <br>The password input mode does not support underlines. <br>If Password Vault is enabled, autofill is available for the username and password. </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-Password = 7--><!--Device-InputType-Password = 7-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NUMBER_PASSWORD

```TypeScript
NUMBER_PASSWORD = 8
```

Number Password entry mode.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>An eye icon is used to show or hide the password. <br>By default, the entered characters are temporarily shown before being obscured by dots; they are directly obscured by dots since API version 12 on certain devices. <br>The password input mode does not support underlines. </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-NUMBER_PASSWORD = 8--><!--Device-InputType-NUMBER_PASSWORD = 8-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## USER_NAME

```TypeScript
USER_NAME = 10
```

UserName entry mode.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If Password Vault is enabled, autofill is available for the username and password. </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-USER_NAME = 10--><!--Device-InputType-USER_NAME = 10-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NEW_PASSWORD

```TypeScript
NEW_PASSWORD = 11
```

NewPassword entry mode.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>An eye icon is used to show or hide the password. <br>By default, the entered characters are temporarily shown before being obscured by dots; they are directly obscured by dots since API version 12 on certain devices. <br>If Password Vault is enabled, a new password can be automatically generated. </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-NEW_PASSWORD = 11--><!--Device-InputType-NEW_PASSWORD = 11-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NUMBER_DECIMAL

```TypeScript
NUMBER_DECIMAL = 12
```

Number decimal entry mode.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The value can contain digits and one decimal point. </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-NUMBER_DECIMAL = 12--><!--Device-InputType-NUMBER_DECIMAL = 12-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## URL

```TypeScript
URL = 13
```

URL entry mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-URL = 13--><!--Device-InputType-URL = 13-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ONE_TIME_CODE

```TypeScript
ONE_TIME_CODE = 14
```

One time code mode.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputType-ONE_TIME_CODE = 14--><!--Device-InputType-ONE_TIME_CODE = 14-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

