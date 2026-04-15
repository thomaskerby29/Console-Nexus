import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 600
    height: 400
    visible: true
    title: "Console Nexus"

    Column {
        width: 600
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        spacing: 10

        Text {
            text: "Setup"
            font.pixelSize: 45
            font.bold: true
            horizontalAlignment: Text.AlignHCenter
            width: parent.width
        }

        Text {
            text: "Console Nexus uses the GitHub API for update checks and downloads.\n" +
                "On public networks, using a Github token is recommended to avoid rate limits.\n" +
                "You can change your token at any time."
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            width: parent.width
        }

        TextField {
            placeholderText: "Token (optional)"
            width: 250
            horizontalAlignment: TextInput.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item {
            width: parent.width
            height: 40

            Row {
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 4

                CheckBox {
                    checked: false
                }

                Text {
                    text: "Encrypt and protect API key locally (recommended)?"
                    wrapMode: Text.WordWrap
                }
            }
        }

        
    }
}