from pyscript import document

def compute_average(event=None):
    scores = []
    for i in range(1, 6):
        val = document.getElementById(f"score{i}").value
        try:
            scores.append(float(val))
        except:
            pass
    if len(scores) == 5:
        avg = sum(scores) / 5
        document.getElementById("average").innerText = f"{avg:.2f}"
        if avg >= 90:
            document.getElementById("result").innerText = "High! 🏆"
        elif avg >= 80:
            document.getElementById("result").innerText = "Average! 👍"
        elif avg >= 75:
            document.getElementById("result").innerText = "Passed! ✅"
    else:
        document.getElementById("average").innerText = ""
        document.getElementById("result").innerText = "Please enter all 5 scores."