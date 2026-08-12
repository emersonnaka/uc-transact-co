const fs = require('fs');
let html = fs.readFileSync('presentation/d3-act2.html', 'utf8');

// The original file has two of these deck-counters because we concatenated poorly or because it was in there twice. Let's fix that.
// But first, let's fix the HTML structure.
html = html.replace(/<div class="deck-counter" aria-hidden="true">\s*<span class="dc-act" id="dcAct">OPENING<\/span>\s*<span><span class="dc-n" id="n">01<\/span> \/ <span id="total">02<\/span><\/span>\s*<span class="dc-bar" id="dcBar"><\/span>\s*<\/div>\s*<nav class="deck-tracker" id="tracker" aria-label="Slide navigation"><\/nav>/g, function(match, offset, string) {
    return offset === string.indexOf(match) ? match : "";
});

fs.writeFileSync('presentation/d3-act2.html', html);
