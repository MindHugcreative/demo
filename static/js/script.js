// Simple JavaScript for any interactive elements

document.addEventListener('DOMContentLoaded', function() {
    // Make challenge cards selectable
    const challengeCards = document.querySelectorAll('.challenge-card');
    
    challengeCards.forEach(card => {
        card.addEventListener('click', function() {
            // Find the radio button inside this card and select it
            const radio = this.querySelector('input[type="radio"]');
            if (radio) {
                radio.checked = true;
                
                // Remove selected class from all cards
                challengeCards.forEach(c => c.classList.remove('selected'));
                
                // Add selected class to this card
                this.classList.add('selected');
            }
        });
    });
    
    // Handle play button in video player
    const playButton = document.querySelector('.play-button');
    if (playButton) {
        playButton.addEventListener('click', function() {
            // In a real app, this would play the video
            // For the demo, we just change the button
            this.textContent = '⏸';
        });
    }
}); 